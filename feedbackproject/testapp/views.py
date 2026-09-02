from django.shortcuts import render
from .forms import FeedbackForm
def feedback_view(request):
    Submitted=False
    name=''
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print('Printing Feedback Information')
            print('*'*50)
            print('Name:',form.cleaned_data['name'])
            print('RollNo:',form.cleaned_data['rollno'])
            print('Email ID:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            Submitted=True
            name=form.cleaned_data['name']
    form=FeedbackForm()
    return render(request,'testapp/index.html',{'form':form,'Submitted':Submitted,'name':name})

