from asyncore import read
from calendar import month
from secrets import choice
from django.db import models
from django.contrib.auth.models import User



class AddIncome(models.Model):
    
    MONTH_CHOICES = (
        ('1', "January"),
        ('2', "February"),
        ('3', "March"),
        ('4', "April"),
        ('4', "May"),
        ('5', "June"),
        ('6', "July"),
        ('7', "August"),
        ('9', "September"),
        ('10', "October"),
        ('11', "November"),
        ('12', "December"),

    )

    income_from = models.CharField(max_length=55, )
    income_amount = models.PositiveIntegerField(default=0)

    month_name = models.CharField(max_length=2, choices=MONTH_CHOICES, default='1')

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    
    def __str__(self):
        return f'{self.income_amount} from {self.income_from}'

 


class CostName(models.Model):
    name = models.CharField(max_length=55, )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )


    def __str__(self):
        return self.name

class MyCost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, )
    name_of_cost = models.CharField(max_length=100, )
    amount_of_cost = models.PositiveIntegerField()
    date_of_cost = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    daily_total_cost = models.PositiveIntegerField(default=0)


    

    def __str__(self):
        return self.name_of_cost