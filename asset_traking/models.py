from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='staffs_user')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='staffs')
    address = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.user} ({self.company})"

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=100)#name of the employee
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.company})"


class Asset(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='assets')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.company})"

class AssetLog(models.Model):
    CHECKOUT_CONDITION_CHOICES = [
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    RETURN_CONDITION_CHOICES = [
        ('good', 'Good'),
        ('damaged', 'Damaged'),
        ('lost', 'Lost'),
    ]

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='logs')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='asset_logs_employee')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='asset_logs_company')

    checkout_quantity = models.SmallIntegerField(default=1)#the asset quantity given to employee
    checkout_time = models.DateTimeField()
    checkout_condition = models.CharField(max_length=10, choices=CHECKOUT_CONDITION_CHOICES, default='good')
    chekout_note = models.TextField(max_length=1000,null=True)
    checkout_by_staff = models.ForeignKey(Staff, on_delete=models.CASCADE,related_name='checkout_staff_logs')

    duration = models.DateField() #The return date for the asset

    is_returned = models.BooleanField(default=False)
    return_time = models.DateTimeField(null=True, blank=True)
    return_quantity = models.SmallIntegerField(default=0)#the quantity returned by employee
    return_condition = models.CharField(max_length=10, choices=RETURN_CONDITION_CHOICES, null=True, blank=True)
    returned_note = models.TextField(max_length=1000,null=True)
    returned_by_staff = models.ForeignKey(Staff, on_delete=models.CASCADE,related_name='returned_staff_logs',null=True)#who received the asset
    issuing_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asset} - {self.employee}"
