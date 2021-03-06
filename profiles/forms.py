from django import forms
from . import models


class BasicDetailsForm(forms.ModelForm):
    # class to store all the model form fields from models.py
    class Meta:
        model = models.BasicDetails
        fields = ["first_name", "middle_name", "last_name", "sex", "DOB",
                  "annual_income", "email", "mobile", "occupation"]

        widgets = {
            'sex': forms.Select(attrs={'class': 'form-control'}),
            # 'job_title':forms.Select(attrs={'class':'form-control'}),
            'DOB': forms.DateInput({'class': 'datepicker'})
        }


class PresentLocationForm(forms.ModelForm):
    class Meta:
        model = models.PresentLocation
        fields = ["country", "state", "city", "street", "pincode"]

        widgets = {
            'state': forms.TextInput(attrs={'placeholder': "States/Province"})
        }


class MoneyTransferForm(forms.ModelForm):
    class Meta:
        model = models.MoneyTransfer
        fields = ["reciprocal_user_name", "reciprocal_account_number", "amount"]
        widgets = {
            'reciprocal_user_name': forms.TextInput(attrs={'style': "height:30px"}),
            'reciprocal_account_number': forms.TextInput(attrs={'style': "height:30px"}),
            'amount': forms.TextInput(attrs={'style': "height:25px"}),
        }


class Loans(forms.ModelForm):
    class Meta:
        model = models.loans
        fields = ['amount', 'loan_type', 'interest_rate', 'date_issue', 'due_date', 'branch_id']
        widgets={
            'loan_type':forms.Select(attrs={'class':'form-control'}),
            'branch_id':forms.Select(attrs={'class':'form-control'})
        }