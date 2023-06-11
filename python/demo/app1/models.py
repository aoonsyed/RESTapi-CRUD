from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=100)
    esalary = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.ename