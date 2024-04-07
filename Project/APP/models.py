from django.db import models

# Model for the description 
class Expense(models.Model):
    Description = models.CharField(max_length=100)
    Expense = models.DecimalField(max_digits=6,decimal_places = 2)
    Payment = models.CharField(max_length=50)
    
    

#Model for the db of the expense type
class Toggle(models.Model):
    ID = models.AutoField(primary_key=True)
    TypeOfExpense = models.CharField(max_length=50)
    