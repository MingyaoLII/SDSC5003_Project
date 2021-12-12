from django.conf.urls import url
from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("account_status/", views.index, name = "account_status"),
    path("money_transfer/", views.money_transfer, name = "money_transfer"),
    path("loan_app/", views.loan, name = "loan_app"),
    path("ewallet/", views.ewallet, name = "ewallet"),
    path("online_pay/", views.online_pay, name = "online_pay"),
    path("settings/", views.settings, name = "settings"),
    path("edit_details/", views.edit_details, name = "edit_details"),
    path("delete_account/", views.delete_account, name = "delete_account")
]
