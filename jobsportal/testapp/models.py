from django.db import models

class hyd_jobs(models.Model):
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    company=models.CharField(max_length=30)
    salary=models.IntegerField()
    location=models.CharField(max_length=30)
    contact=models.BigIntegerField()
