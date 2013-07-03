from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=30)
    cappath = models.CharField(max_length=100)
    logfile = models.CharField(max_length=100) 
    dlock = models.IntegerField(max_length=20) 
    rlock = models.IntegerField(max_length=20) 
    lastupdatetime = models.DateTimeField()

    def __unicode__(self):
        return self.name

class IntervalsSetting(models.Model):
    name = models.CharField(max_length=30)
    deploytimeintervals = models.IntegerField(max_length=20)
    rollbacktimeintervals = models.IntegerField(max_length=20)

class Operation(models.Model):
    name = models.CharField(max_length=30)
    command = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=11)
    email = models.EmailField(verbose_name='e-mail')

    def __unicode__(self):
        return self.name
