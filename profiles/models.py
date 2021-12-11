from django.db import models
from django.utils import timezone
import datetime


class BasicDetails(models.Model):
    # (Name, Sex, DOB, Annual income, Email, Mobile number, Occupation)
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=None)
    sex = models.CharField(max_length=1, default=None, help_text='M: Male or F: Female')
    annual_income = models.IntegerField(default=0)
    email = models.EmailField(default=None)
    mobile = models.IntegerField(default=0)
    occupation = models.CharField(max_length=50, default=None)
    DOB = models.DateField(default=None)
    user_name = models.CharField(max_length=150, default=None)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    job_title = models.CharField(max_length=150, help_text="employee/manager",null = True)
    max_loan_auth = models.DecimalField(max_digits=10, decimal_places=2, help_text="The maximum loan authority of the employee",
                                        null = True)

    def __str__(self):
        return self.user_name


class PresentLocation(models.Model):
    # (Country, State, City, Street, Pincode)
    country = models.CharField(max_length=50, default="China")
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    pincode = models.IntegerField()
    user_name = models.CharField(max_length=150, default=None)

    def __str__(self):
        return self.user_name


class Status(models.Model):
    """
       interest_rate: default to be 0.03
       overdraft_limit_quarterly: The maximum number of overdraft, default to be 5
       overdraft_interest_rate: Interest rate charges on the overdraft part
    """
    account_number = models.IntegerField(primary_key=True)
    balance = models.IntegerField()
    user_name = models.CharField(max_length=150, default=None)
    interest_rate = models.DecimalField(default=0.05, max_digits=3, decimal_places=2)
    overdraft_limit_quarterly = models.IntegerField(default=5)
    overdraft_interest_rate = models.DecimalField(default=0.15, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.account_number


class MoneyTransfer(models.Model):
    enter_your_user_name = models.CharField(max_length=150, default=None)
    enter_the_destination_account_number = models.IntegerField()
    enter_the_amount_to_be_transferred_in_INR = models.IntegerField()

    def __str__(self):
        return self.enter_your_user_name

class branches(models.Model):
    bid = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 150, help_text="The name of the Branch")
    address = models.CharField(max_length=150, help_text="The address of the Branch")
    phone_num = models.CharField(max_length=8, help_text="HongKong Phone number")

    def __str__(self):
        return self.name


def six_month_after():
    return timezone.now() + timezone.timedelta(days=180)

class loans(models.Model):
    lid = models.AutoField(primary_key = True)
    amount = models.IntegerField()
    interest_rate = models.DecimalField(default=0.05,max_digits=3, decimal_places=2)
    date_issue = models.DateField(default=timezone.now)
    due_date = models.DateField(default=six_month_after())
    TYPE = [('Car', 'car loan'), ('Hou', 'house loan'),('Oth', 'Other loan'),]
    loan_type = models.CharField(max_length=3, choices=TYPE, default=None)
    customer_id = models.ForeignKey(BasicDetails, on_delete=models.DO_NOTHING)
    branch_id = models.ForeignKey(branches, on_delete=models.DO_NOTHING)

