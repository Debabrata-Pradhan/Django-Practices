import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'jobsportal.settings')
import django
django.setup()
from faker import Faker
from random import *
from testapp.models import hyd_jobs
fake=Faker()
def sal():
    salary=randint(100000,1000000)
    return salary
def phnogen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        ftitle=fake.random_elements(elements=('L1 lead','Team Lead','SDE1','SE1'))
        feligibility=fake.random_element(elements=('B.Tech','MCA','BCA','M.Tech'))
        fcompany=fake.company()
        fsalary=sal()
        flocation=fake.address()
        fcontact=phnogen()
        hyd_jobs_record=hyd_jobs.objects.get_or_create(
            title=ftitle,
            eligibility=feligibility,
            company=fcompany,
            salary=fsalary,
            location=flocation,
            contact=fcontact
        )
n=int(input("Enter how many records you want to push:"))
populate(n)
print("Records are inserted Successfully.")






