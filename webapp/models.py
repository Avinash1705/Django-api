from pyexpat import model
from django.db import models

# Create your models here.
class emplyoees(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def _str_(self):
        return self.firstname