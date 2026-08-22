from django.contrib import admin
from testapp.models import seed1
class seed1Admin(admin.ModelAdmin):
    list_display=['rollno','sname','email','dob','marks','phno','addr']
admin.site.register(seed1,seed1Admin)
