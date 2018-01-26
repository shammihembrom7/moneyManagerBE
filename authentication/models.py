from __future__ import unicode_literals
from django.db import models


class Users(models.Model):
    usertype_choice = (
        ('Patient','patient'),
        ('Doctor','doctor'),
        ('Staff','Staff'),
        ('Clinic','clinic'),
    )
    user_name = models.CharField(max_length=255,null=True,blank=True)
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=400, null=True)
    mobile_number = models.IntegerField(db_column='mobileNumber', blank=True, null=True)
    otp_verification = models.IntegerField(db_column='otpVerification', blank=True, null=True)
    email_verified = models.IntegerField(db_column='email_verified', blank=True, null=True)
    usertype = models.CharField(max_length=255, blank=True, null=True,choices=usertype_choice)
    created_at = models.DateTimeField(auto_now_add=True,  db_column='createdAt')
    updated_at = models.DateTimeField(auto_now_add=True, db_column='updatedAt')

    class Meta:
        managed = True
        db_table = 'users'


class OtpLogs(models.Model):
    otp_code = models.CharField(db_column='otpCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    purpose = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'otpLogs'
