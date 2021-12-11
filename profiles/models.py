from django.db import models
import datetime


class BasicDetails(models.Model):
    # (Name, Sex, DOB, Annual income, Email, Mobile number, Occupation)
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=None)
    SEX = (('M', 'Male'),('F', 'Female'),)

    sex = models.CharField(max_length = 1,choices=SEX, default = None)
    annual_income = models.IntegerField(default=0)
    email = models.EmailField(default=None)
    mobile = models.IntegerField(default=0)
    occupation = models.CharField(max_length=50, default=None)
    DOB = models.DateField(default=None)
    user_name = models.CharField(max_length=150, default=None)

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
    account_number = models.IntegerField()
    balance = models.IntegerField()
    user_name = models.CharField(max_length=150, default=None)
    interest_rate = models.FloatField(default=0.05)
    overdraft_limit_quarterly = models.IntegerField(default=5)
    overdrate_interest_rate = models.FloatField(default=0.15)

    def __str__(self):
        return self.account_number


class MoneyTransfer(models.Model):
    enter_your_user_name = models.CharField(max_length=150, default=None)
    enter_the_destination_account_number = models.IntegerField()
    enter_the_amount_to_be_transferred_in_INR = models.IntegerField()

    def __str__(self):
        return self.enter_your_user_name
