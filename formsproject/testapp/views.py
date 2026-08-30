from django.shortcuts import render

from testapp.forms import StudentForm


def forms_view(request):
    Submitted = False
    name=''
    if request.method=='POST':
        form =StudentForm(request.POST)
        if form.is_valid():
            print('Form validation success and print data')
            print('Name:',form.cleaned_data['name'])
            print('RollNo.:',form.cleaned_data['rollno'])
            print('Marks:',form.cleaned_data['marks'])
            Submitted=True
            name=form.cleaned_data['name']
    form = StudentForm()
    return render(request,'testapp/index.html',{'form':form,'Submitted':Submitted,'name':name})
