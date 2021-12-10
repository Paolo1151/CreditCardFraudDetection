from django.shortcuts import render, redirect
from sklearn.compose import ColumnTransformer

from . import forms

import joblib
import os
import pandas as pd
import numpy as np
import xgboost as xgb
 
from ColumnTransformer.Transformers import *

columns = ['ssn',
    'cc_num',
    'first',
    'last',
    'gender',
    'street',
    'city',
    'state',
    'zip',
    'lat',
    'long',
    'city_pop',
    'job',
    'dob',
    'acct_num',
    'trans_num',
    'trans_date',
    'trans_time',
    'unix_time',
    'category',
    'amt',
    'merchant',
    'merch_lat',
    'merch_long'
]

funcs = [
    clean_data,
    transform_credit_card,
    transform_age,
    transform_distance,
    transform_holidays,
    label_objects,
    drop_columns
]

bst = xgb.Booster({'nthread': 4})
bst.load_model(os.path.join(os.getcwd(), 'models/model_xgboost.json'))

def fraud_detection(request):
    if request.method == 'GET':
        if not 'result' in request.session:
            request.session['result'] = 'None' 
        form = forms.FraudDetectionForm()
        return render(request, 'FraudDetection/fraud-form.html', {'form': form, 'Error':False})
    elif request.method == 'POST':
        form = forms.FraudDetectionForm(request.POST)
        if form.is_valid():
            data = request.POST.dict()
            entry = pd.DataFrame(data, index=[0])
            entry.drop(columns=['csrfmiddlewaretoken'], inplace=True)

            columns = ['cc_num', 'zip', 'lat', 'long', 'city_pop', 'acct_num', 'unix_time', 'amt', 'merch_lat', 'merch_long']
            dtypes = [np.int64, np.int64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64]

            for col, dtyp in zip(columns, dtypes):
                entry[col] = entry[col].astype(dtype=dtyp)

            for func in funcs:
                entry = func(entry)

            dmat = xgb.DMatrix(entry)

            result = round(bst.predict(dmat)[0])

            request.session['result'] = 'Fraud' if result == 1 else 'Not Fraud'
            return redirect('/fraud-detection')
        else:
            return render(request, 'FraudDetection/fraud-form.html', {'Error': 'Invalid Form'})
