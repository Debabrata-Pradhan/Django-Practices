from django.db import models
class seed1(models.Model):
    rollno=models.IntegerField()
    sname=models.CharField(max_length=30)
    email=models.EmailField()
    dob=models.DateField()
    marks=models.IntegerField()
    phno=models.BigIntegerField()
    addr=models.TextField()


