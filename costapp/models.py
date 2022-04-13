from django.db import models
from django.contrib.auth.models import User

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