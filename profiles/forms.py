from django import forms
from . import models


class BasicDetailsForm (forms.ModelForm):
    # class to store all the model form fields from models.py
    class Meta:
        model = models.BasicDetails
        fields = ["first_name", "middle_name", "last_name", "sex", "DOB", "annual_income", "email", "mobile", "occupation",]

        widgets = {
            'sex': forms.Select(attrs={'class': 'form-control'}),
            # 'job_title':forms.Select(attrs={'class':'form-control'}),
            'DOB': forms.DateInput({'class':'datepicker'})
        }


class PresentLocationForm (forms.ModelForm):
    class Meta:
        model = models.PresentLocation
        fields = ["country", "state", "city", "street", "pincode"]

        widgets = {
            'state' :forms.TextInput(attrs={'placeholder':"States/Province"})
        }


class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = models.MoneyTransfer
        fields = [
            "user_name",
            "account_number",
            "reciprocal_user_name",
            "reciprocal_account_number",
            "amount",
        ]


class Loans (forms.ModelForm):
    class Meta:
        model = models.loans
        fields = ['customer_id',
                  'amount',
                  'interest_rate',
                  'date_issue',
                  'due_date',
                  'loan_type',
                  'customer_id',
                  'branch_id']