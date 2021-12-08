from django.shortcuts import render, redirect

from . import forms

import joblib
import os
import pandas as pd
import numpy as np

def fraud_detection(request):
    if request.method == 'GET':
        if not 'result' in request.session:
            request.session['result'] = 'None' 
        form = forms.FraudDetectionForm()
        return render(request, 'FraudDetection/fraud-form.html', {'form': form, 'Error':False})
    elif request.method == 'POST':
        form = forms.FraudDetectionForm(request.POST)
        if form.is_valid():
            # data = pd.DataFrame()

            # model = joblib.load(os.path.join(os.getcwd(), '/../models/final_model.joblib'))
            # result = model.predict()
            request.session['result'] = 'Not Implemented' # TODO
            return redirect('/fraud-detection')
        else:
            return render(request, 'FraudDetection/fraud-form.html', {'Error': 'Invalid Form'})
