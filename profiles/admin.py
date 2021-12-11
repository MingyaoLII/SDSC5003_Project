from django.contrib import admin
from .models import *


# Define the admin class
class BasicDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'user_name')


class PresentLocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'state', 'city', 'user_name')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'balance', 'user_name')


class MoneyTransferAdmin(admin.ModelAdmin):
    list_display = ('enter_your_user_name', 'enter_the_destination_account_number',
                    'enter_the_amount_to_be_transferred_in_INR')


# Register the admin class with the associated model
admin.site.register(BasicDetails, BasicDetailsAdmin)
admin.site.register(PresentLocation, PresentLocationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(MoneyTransfer, MoneyTransferAdmin)
