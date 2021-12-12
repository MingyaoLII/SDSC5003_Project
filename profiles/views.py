from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from profiles.models import Status, MoneyTransfer
import random


def randomGen():
    # return a 6 digit random number
    return int(random.uniform(100000, 999999))


def index(request):
    try:
        curr_user = Status.objects.get(user_name=request.user)  # getting details of current user
    except:
        # if no details exist (new user), create new details
        curr_user = Status()
        # curr_user.account_number = randomGen()  # random account number for every new user
        curr_user.balance = 0
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "profiles/profile.html", {"curr_user": curr_user})


def money_transfer(request):
    if request.method == "POST":
        form = forms.MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()

            transfer = models.MoneyTransfer.objects.get(user_name=request.user)
            reciprocal_user_name = transfer.reciprocal_user_name

            transfer_amount = transfer.amount  # FIELD 1
            reciprocal_user = models.Status.objects.get(user_name=reciprocal_user_name)  # FIELD 2
            curr_user = models.Status.objects.get(user_name=request.user)  # FIELD 3

            if curr_user.balance >= transfer_amount:
                # Now transfer the money!
                curr_user.balance = curr_user.balance - transfer_amount
                reciprocal_user.balance = reciprocal_user.balance + transfer_amount

                # Save the changes before redirecting
                transfer.save()
                reciprocal_user.save()
                curr_user.save()

        return redirect("profiles/profile.html")
    else:
        form = forms.MoneyTransferForm()
    return render(request, "profiles/money_transfer.html", {"form": form})


def loan(request):
    return render(request, "profiles/loans.html")


def ewallet(request):
    return render(request, "profiles/eWallet.html")


def online_pay(request):
    return render(request, "profiles/online_payment.html")


def settings(request):
    return render(request, "profiles/settings.html")


def edit_details(request):
    if request.method == "POST":
        # POST actions for BasicDetailsForms
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form = forms.BasicDetailsForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.BasicDetailsForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()

        # POST actions for PresentLocationForm
        try:
            curr_user = models.PresentLocation.objects.get(user_name=request.user)
            form = forms.PresentLocationForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.PresentLocationForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()

                # POST actions for Password change
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

        return redirect("profiles/edit_details.html")

    else:  # GET actions
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form1 = forms.BasicDetailsForm(instance=curr_user)  # basic details
        except:
            form1 = forms.BasicDetailsForm()

        try:
            curr_user = models.PresentLocation.objects.get(user_name=request.user)
            form2 = forms.PresentLocationForm(instance=curr_user)  # location
        except:
            form2 = forms.PresentLocationForm()

        # change password
        form3 = PasswordChangeForm(request.user)

        dici = {"form1": form1, "form2": form2, "form3": form3}
        return render(request, "profiles/edit_details.html", dici)


def delete_account(request):
    return render(request, "profiles/delete_account.html")
