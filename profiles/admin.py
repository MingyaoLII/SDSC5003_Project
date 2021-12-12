from django.contrib import admin
from .models import *


# Define the admin class
class BasicDetailsAdmin(admin.ModelAdmin):
    list_display = ('uid', 'first_name', 'middle_name', 'last_name', 'sex', 'email', 'mobile', 'user_name')
    ordering = ('uid', 'first_name', 'middle_name', 'last_name')


class PresentLocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'state', 'city', 'user_name')
    ordering = ['country']


class StatusAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'balance', 'user_name')
    ordering = ['account_number']


class MoneyTransferAdmin(admin.ModelAdmin):
    list_display = ('transfer_id', 'amount', 'reciprocal_user_name',
                    'reciprocal_account_number', 'datetime')
    ordering = ['transfer_id']


class LoanAdmin(admin.ModelAdmin):
    list_display = ('lid', 'amount', 'loan_type', 'due_date')
    ordering = ['due_date']


class BranchAdmin(admin.ModelAdmin):
    list_display = ('bid', 'name', 'address', 'phone_num')
    ordering = ['name']


# Register the admin class with the associated model
admin.site.register(BasicDetails, BasicDetailsAdmin)
admin.site.register(PresentLocation, PresentLocationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(MoneyTransfer, MoneyTransferAdmin)
admin.site.register(loans, LoanAdmin)
admin.site.register(branches, BranchAdmin)
