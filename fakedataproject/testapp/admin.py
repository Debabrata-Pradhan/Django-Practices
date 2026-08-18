from django.contrib import admin

from testapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=[
        'rollno','name','dob','marks','email','phno','addr'
    ]
admin.site.register(Student,StudentAdmin)
