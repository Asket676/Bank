from django.db import models

# Create your models here.

    
class BankClients(models.Model):
    surname = models.CharField(max_length=20,blank=False)
    name = models.CharField(max_length=20,blank=False)
    secondName = models.CharField(max_length=20,blank=False)

    def __str__(self):
        return f'{self.surname}{self.name}{self.secondName}'
    
class BankWorkers(models.Model):
    surname = models.CharField(max_length=20,blank=False)
    name = models.CharField(max_length=20,blank=False)
    secondName = models.CharField(max_length=20,blank=False)
    job = models.CharField(max_length=20,blank=False)
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.surname}{self.name}{self.secondName}'

class InvestType(models.Model):
    name = models.CharField(max_length=20,blank=False)
    minTime = models.IntegerField(blank=False)
    minAmount = models.IntegerField(blank=False)
    code = models.CharField(max_length=20,blank=False)
    percent = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.name}'

class MoneyCourse(models.Model):
    name = models.CharField(max_length=20,blank=False)
    course = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.name}'

class InvestRegist(models.Model):
    client = models.CharField(max_length=20,blank=False)
    code = models.IntegerField(blank=False)
    dateIn = models.CharField(max_length=20,blank=False)
    dateOut = models.CharField(max_length=20,blank=False)
    amount = models.IntegerField(blank=False)
    status = models.CharField(max_length=20,blank=False)
    worker = models.CharField(max_length=20,blank=False)

    def __str__(self):
        return f'{self.client}'


    
"""makemigrations migrate"""
"""runserver"""