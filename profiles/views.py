from django.http import QueryDict
from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from profiles.models import Status, MoneyTransfer, loans
from .forms import MoneyTransferForm
from django.contrib import messages


def toast(request):
    messages.success(request, "Success!")


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
        form = MoneyTransferForm(request.POST)
        if form.is_valid():
            transfer = MoneyTransfer()
            transfer.user_name = request.user.username
            temp = Status.objects.filter(user_name=request.user.username)
            transfer.account_number = temp.values("account_number")
            transfer.reciprocal_user_name = form.cleaned_data['reciprocal_user_name']
            transfer.reciprocal_account_number = form.cleaned_data['reciprocal_account_number']
            transfer.amount = form.cleaned_data['amount']

            reciprocal_user_name = form.cleaned_data['reciprocal_user_name']
            transfer_amount = form.cleaned_data['amount']  # FIELD 1
            reciprocal_user = models.Status.objects.get(user_name=reciprocal_user_name)  # FIELD 2
            curr_user = models.Status.objects.get(user_name=request.user)  # FIELD 3
            # Now transfer the money!
            curr_user.balance = curr_user.balance - transfer_amount
            reciprocal_user.balance = reciprocal_user.balance + transfer_amount

            # Save the changes before redirecting
            transfer.save()
            reciprocal_user.save()
            curr_user.save()
        return redirect("profiles/profile.html")
    form = forms.MoneyTransferForm()
    return render(request, "profiles/money_transfer.html", {"form": form})


def loans(request):
    if request.method == "POST":
        curr_user = models.BasicDetails.objects.get(user_name=request.user)
        print('request post', request.POST)
        # eceive_dict = QueryDict.copy(request.POST)
        # receive_dict['customer_id'] = '1'
        # print('receive dict', receive_dict)
        form = forms.Loans(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.customer_id = curr_user
            post.save()
    form = forms.Loans()
    # print('form ', form)
    return render(request, "profiles/loans.html", {"form": form})


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
