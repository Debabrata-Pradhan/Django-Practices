import os
import sys
import django

current_dir = os.path.dirname(os.path.abspath(__file__))

project_root = os.path.dirname(current_dir)

sys.path.append(project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakedataproject.settings')

django.setup()

from testapp.models import Student

from faker import Faker
from random import *
def phnogen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fake=Faker()
        frollno=fake.random_int(min=1,max=999)
        fname=fake.name()
        fdob=fake.date()
        fmarks=fake.random_int(min=1,max=100)
        femail=fake.email()
        fphno=phnogen()
        faddr=fake.address()
        Student.objects.get_or_create(
            rollno=frollno,
            name=fname,
            dob=fdob,
            marks=fmarks,
            email=femail,
            phno=fphno,
            addr=faddr

        )
n=int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted successfully.')
