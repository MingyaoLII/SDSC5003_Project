from django import forms
from . import models


<<<<<<< Updated upstream
class BasicDetailsForm (forms.ModelForm):
=======
class BasicDetailsForm(forms.ModelForm):
>>>>>>> Stashed changes
    # class to store all the model form fields from models.py
    class Meta:
        model = models.BasicDetails
        fields = ["first_name", "middle_name", "last_name", "sex", "DOB", "annual_income", "email", "mobile", "occupation"]

        widgets = {
            'sex': forms.Select(attrs={'class': 'form-control'}),
        }


<<<<<<< Updated upstream
class PresentLocationForm (forms.ModelForm):
=======
class PresentLocationForm(forms.ModelForm):
>>>>>>> Stashed changes
    class Meta:
        model = models.PresentLocation
        fields = ["country", "state", "city", "street", "pincode"]


<<<<<<< Updated upstream
class MoneyTransferForm (forms.ModelForm):
=======
class MoneyTransferForm(forms.ModelForm):
>>>>>>> Stashed changes
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
        fields = ['lid',
                  'amount',
                  'interest_rate',
                  'date_issue',
                  'due_date',
                  'loan_type',
                  'customer_id',
                  'branch_id']