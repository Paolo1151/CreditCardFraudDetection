from django import forms

class FraudDetectionForm(forms.Form):
    ssn = forms.CharField(label='Social Security No.', max_length=255)
    cc_num = forms.CharField(label='Credit Card No.', max_length=255)

    first = forms.CharField(label='First Name', max_length=255)
    last = forms.CharField(label='Last Name', max_length=255)

    gender = forms.CharField(label='Gender', max_length=255)

    street = forms.CharField(label='Street', max_length=255)
    city = forms.CharField(label='City', max_length=255)
    state = forms.CharField(label='State', max_length=255)
    zip = forms.CharField(label='Zip Code', max_length=20)

    lat = forms.CharField(label='Latitude', max_length=255)
    long = forms.CharField(label = 'Longitude', max_length=255)

    city_pop = forms.CharField(label='City Population', max_length=255)

    job = forms.CharField(label='Job', max_length=255)
    dob = forms.CharField(label='Date of Birth', max_length=255)
    
    acct_num = forms.CharField(label='Account Number')
    trans_num = forms.CharField(label='Transaction Number')
    trans_date = forms.CharField(label='Transaction Date')
    trans_time = forms.CharField(label='Transaction Time')
    unix_time = forms.CharField(label='Unix Time')

    category = forms.CharField(label='Category')
    amt = forms.CharField(label='Amount')

    merchant = forms.CharField(label='Merchant')
    merch_lat = forms.CharField(label='Merchant Latitude')
    merch_long = forms.CharField(label='Merchant Longitude')
