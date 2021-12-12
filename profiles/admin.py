from django.contrib import admin
from .models import *


# Define the admin class
class BasicDetailsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'mobile', 'user_name')


class PresentLocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'state', 'city', 'user_name')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'balance', 'user_name')


class MoneyTransferAdmin(admin.ModelAdmin):
    list_display = ('transfer_id', 'amount', 'account_number',
                    'reciprocal_user_name', 'reciprocal_account_number',)


class LoanAdmin(admin.ModelAdmin):
    list_display = ('lid', 'amount')


class BranchAdmin(admin.ModelAdmin):
    list_display = ('bid', 'name')


# Register the admin class with the associated model
admin.site.register(BasicDetails, BasicDetailsAdmin)
admin.site.register(PresentLocation, PresentLocationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(MoneyTransfer, MoneyTransferAdmin)
admin.site.register(loans, LoanAdmin)
admin.site.register(branches, BranchAdmin)
