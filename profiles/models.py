from django.db import models
from django.utils import timezone
import datetime


class BasicDetails(models.Model):
    # (Name, Sex, DOB, Annual income, Email, Mobile number, Occupation)
    uid = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=150, default=None)
    first_name = models.CharField(max_length=50, default=None)
    middle_name = models.CharField(max_length=50, default=None, null=True)
    last_name = models.CharField(max_length=50, default=None)
    SEX = (('M', 'Male'), ('F', 'Female'),)
    sex = models.CharField(max_length=1, choices=SEX, default=None)
    annual_income = models.IntegerField(default=0, null=True)
    email = models.EmailField(default=None)
    mobile = models.CharField('Hong Kong phone number', max_length=8)
    occupation = models.CharField(max_length=50, default=None)
    DOB = models.DateField('Date of birth', default=None)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    JOB = (('employee', 'employee'), ('manager', 'manager'))
    job_title = models.CharField(max_length=150, choices=JOB, null=True, blank=True)
    max_loan_auth = models.DecimalField(max_digits=10, decimal_places=2,
                                        # help_text="The maximum loan authority of the employee",
                                        null=True, blank=True)

    def __str__(self):
        return str(self.uid)


class PresentLocation(models.Model):
    # (Country, State, City, Street, Pincode)
    country = models.CharField(max_length=50, default="China")
    state = models.CharField(max_length=50, help_text='States/Province')
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    pincode = models.IntegerField()
    user_name = models.CharField(max_length=150, default=None)

    def __str__(self):
        return self.country


class Status(models.Model):
    """
       interest_rate: default to be 0.03
       overdraft_limit_quarterly: The maximum number of overdraft, default to be 5
       overdraft_interest_rate: Interest rate charges on the overdraft part
    """
    account_number = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    user_name = models.CharField(max_length=150, default=None)
    interest_rate = models.DecimalField(default=0.05, max_digits=3, decimal_places=2)
    overdraft_limit_quarterly = models.IntegerField(default=5)
    overdraft_interest_rate = models.DecimalField(default=0.15, max_digits=3, decimal_places=2)

    def __str__(self):
        return str(self.account_number)


class MoneyTransfer(models.Model):
    transfer_id = models.BigAutoField(primary_key=True)
    datetime = models.DateTimeField(default=timezone.now)
    user_name = models.CharField(max_length=150)
    account_number = models.IntegerField()
    reciprocal_user_name = models.CharField(max_length=150, default=None)
    reciprocal_account_number = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.transfer_id)


class branches(models.Model):
    bid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, help_text="The name of the Branch")
    address = models.CharField(max_length=150, help_text="The address of the Branch")
    phone_num = models.CharField(max_length=8, help_text="HongKong Phone number")

    def __str__(self):
        return self.name


def six_month_after():
    return timezone.now() + timezone.timedelta(days=180)


class loans(models.Model):
    lid = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    interest_rate = models.DecimalField(default=0.05, max_digits=3, decimal_places=2)
    date_issue = models.DateField(default=timezone.now)
    due_date = models.DateField(default=six_month_after())
    TYPE = [('Car', 'car loan'), ('Hos', 'house loan'), ('Oth', 'other loan'), ]
    loan_type = models.CharField(max_length=3, choices=TYPE, default=None)
    customer_id = models.ForeignKey(BasicDetails, on_delete=models.DO_NOTHING)
    branch_id = models.ForeignKey(branches, on_delete=models.DO_NOTHING)

    def __int__(self):
        return self.lid
