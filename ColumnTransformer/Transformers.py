from sklearn.preprocessing import LabelEncoder
from geopy.distance import geodesic

import pandas as pd
import datetime
import re

##################

import re

visa_regex = r'^4'
mc_regex = r'^5[1-5]|222[1-9]|22[3-9][0-9]|2[3-6][0-9]|27[01][0-9]|2720'
jcb_regex = r'^352[8-9]|35[3-8][0-9]'
amex_regex = r'^34|37'

to_drop = [
    'ssn', 
    'cc_num', 
    'acct_num', 
    'first', 
    'last', 
    'street', 
    'state', 
    'unix_time', 
    'trans_num', 
    'job',
    'zip', 
    'city', 
    'trans_date', 
    'trans_time', 
    'unix_time', 
    'dob', 
    'lat', 
    'long', 
    'merch_lat', 
    'merch_long'
]

holiday_dict = dict()

def _generate_holidays(row_year):
    holidays = set([datetime.datetime(row_year, 12, 25), datetime.datetime(row_year, 2, 14)])
    for i in range(12):
        holidays.add(datetime.datetime(row_year, i+1, i+1))
    
    mothersday = [datetime.datetime(2021, 5, i) for i in range(1,32) if datetime.datetime(2021, 5, i).weekday() == 6][0]
    fathersday = [datetime.datetime(2021, 6, i) for i in range(1,31) if datetime.datetime(2021, 6, i).weekday() == 6][0]

    holidays.add(mothersday)
    holidays.add(fathersday)

    holidays = sorted(list(holidays))
    return holidays

def _calculate_dist_next_holiday(row):
    row_year = row['trans_date'].year

    if not row_year in holiday_dict:
        holiday_dict[row_year] = _generate_holidays(row_year)
        
    for holi in holiday_dict[row_year]:
        if row['trans_date'] <= holi:
            row['days_to_next_holiday'] = (holi - row['trans_date']).days
            break
    return row

def _calculate_distance(row):
    home_tup = (row['lat'], row['long'])
    merch_tup = (row['merch_lat'], row['long'])
    row['distance'] = geodesic(home_tup, merch_tup).km
    return row

def _categorize(row):
    if re.search(visa_regex, row['cc_num']):
        row['cc_cat'] = 'VISA'
    elif re.search(mc_regex, row['cc_num']):
        row['cc_cat'] = 'MASTERCARD'
    elif re.search(jcb_regex, row['cc_num']):
        row['cc_cat'] = 'JCB'
    elif re.search(amex_regex, row['cc_num']):
        row['cc_cat'] = 'AMEX'
    else:
        row['cc_cat'] = 'OTHER'
    return row


##################

def transform_age(df):
    temp = df.copy()
    temp['age'] = (datetime.datetime.now().year - temp['dob'].dt.year)
    return temp

def transform_holidays(df):
    temp = df.copy()
    temp = temp.apply(_calculate_dist_next_holiday, axis=1)
    return temp

def label_objects(df):
    temp = df.copy()
    le = LabelEncoder()
    for col in temp.columns:
        if temp[col].dtype == object:
            temp[col] = le.fit_transform(temp[col])
    return temp

def transform_distance(df):
    temp = df.copy()
    temp = temp.apply(_calculate_distance, axis=1)
    return temp

def drop_columns(df):
    return df.drop(columns=to_drop)

def transform_credit_card(df):
    temp = df.copy()
    temp['cc_num'] = temp['cc_num'].astype(str)
    temp = temp.apply(_categorize, axis=1)
    return temp

def clean_data(df):
    temp = df.copy()
    temp['trans_date'] = pd.to_datetime(temp['trans_date'])
    temp['dob'] = pd.to_datetime(temp['dob'])
    temp['trans_time'] = pd.to_datetime(temp['trans_time'])
    return temp
