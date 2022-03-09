import code
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
#always put master tables first

class vm_vh_class(models.Model):
    code = models.IntegerField(primary_key=True, default=0)
    descr = models.CharField(max_length=100, blank=False, null=False, default='NA')
    transport_catg = models.CharField(max_length=2, blank=True, null=True) #added new field
    def __str__(self):
        return self.code

class vt_owner(models.Model):
    regn_no = models.CharField(max_length=10, primary_key=True)
    owner_name = models.CharField(max_length=35, null=False)
    regn_dt = models.DateField(null=False)
    no_cyl = models.IntegerField(null=False)
    vh_class = models.ForeignKey(vm_vh_class, on_delete=models.CASCADE, default=0) #foreign key