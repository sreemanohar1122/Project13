from django.db import models

class Jobs(models.Model):
    jobid=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    skills=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
# Create your models here.
