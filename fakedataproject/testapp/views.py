from django.shortcuts import render
from testapp.models import Student
def student_view(request):
    student_list=Student.objects.all()
    return render(request,'testapp/index.html',{'student_list':student_list})
