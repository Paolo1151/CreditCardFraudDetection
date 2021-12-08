from django import forms

class FraudDetectionForm(forms.Form):
    ssn = forms.CharField(label='Social Security No.', max_length=255)
    cc_num = forms.IntegerField(label='Credit Card No.')

    first = forms.CharField(label='First Name', max_length=255)
    last = forms.CharField(label='Last Name', max_length=255)

    gender = forms.CharField(label='Gender', max_length=1)

    street = forms.CharField(label='Street', max_length=255)
    city = forms.CharField(label='City', max_length=255)
    state = forms.CharField(label='State', max_length=255)
    zipcode = forms.CharField(label='Zip Code', max_length=20)

    lat = forms.FloatField(label='Latitude')
    long = forms.FloatField(label = 'Longitude')

    city_pop = forms.IntegerField(label='City Population')

    job = forms.CharField(label='Job')
    date_of_birth = forms.DateTimeField(label='Date of Birth')
    
    acct_num = forms.IntegerField(label='Account Number')
    trans_num = forms.IntegerField(label='Transaction Number')
    trans_date = forms.DateField(label='Transaction Date')
    trans_time = forms.DateTimeField(label='Transaction Time')
    unix_time = forms.DateTimeField(label='Unix Time')

    category = forms.CharField(label='Category')
    amt = forms.FloatField(label='Amount')

    merchant = forms.CharField(label='Merchant')
    merchant_lat = forms.FloatField(label='Merchant Latitude')
    merchant_long = forms.FloatField(label='Merchant Longitude')
