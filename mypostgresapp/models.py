from asyncio.windows_events import NULL
from msilib.schema import Class
from django.db import models

# Create your models here.
class vt_owner(models.Model):
    regn_no = models.CharField(max_length=10, primary_key=True)
    owner_name = models.CharField(max_length=35, null=False)
    regn_dt = models.DateField(null=False)
    no_cyl = models.IntegerField(null=False)
