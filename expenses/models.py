from django.db import models

class Expense(models.Model):
    amount=models.DecimalField(max_digits=12 , decimal_places=2)
    date_time=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=200)
