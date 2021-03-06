# Generated by Django 3.1.2 on 2021-12-13 19:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicDetails',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('annual_income', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=8, verbose_name='Hong Kong phone number')),
                ('occupation', models.CharField(max_length=50)),
                ('DOB', models.DateField(verbose_name='Date of birth')),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('job_title', models.CharField(blank=True, choices=[('E', 'employee'), ('M', 'manager')], max_length=150, null=True)),
                ('max_loan_auth', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='branches',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='The name of the Branch', max_length=150)),
                ('address', models.CharField(help_text='The address of the Branch', max_length=150)),
                ('phone_num', models.CharField(help_text='HongKong Phone number', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyTransfer',
            fields=[
                ('transfer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_name', models.CharField(max_length=150)),
                ('account_number', models.IntegerField()),
                ('reciprocal_user_name', models.CharField(default=None, max_length=150)),
                ('reciprocal_account_number', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PresentLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('user_name', models.CharField(default=None, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('account_number', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
                ('user_name', models.CharField(default=None, max_length=150)),
                ('interest_rate', models.DecimalField(decimal_places=2, default=0.05, max_digits=3)),
                ('overdraft_limit_quarterly', models.IntegerField(default=5)),
                ('overdraft_interest_rate', models.DecimalField(decimal_places=2, default=0.15, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='loans',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('interest_rate', models.DecimalField(decimal_places=2, default=0.05, max_digits=3)),
                ('date_issue', models.DateField(default=django.utils.timezone.now)),
                ('due_date', models.DateField(default=datetime.datetime(2022, 6, 11, 19, 16, 27, 531107, tzinfo=utc))),
                ('loan_type', models.CharField(choices=[('Car', 'car loan'), ('Hos', 'house loan'), ('Oth', 'other loan')], default=None, max_length=3)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.branches')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profiles.basicdetails')),
            ],
        ),
    ]
