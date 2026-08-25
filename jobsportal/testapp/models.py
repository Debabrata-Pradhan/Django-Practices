from django.db import models

class hyd_jobs(models.Model):
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    salary=models.IntegerField()
    location=models.CharField(max_length=100)
    contact=models.BigIntegerField()
