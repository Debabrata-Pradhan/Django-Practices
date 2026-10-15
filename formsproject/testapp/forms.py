from django import forms
class StudentForm(forms.Form):
    name= forms.CharField(max_length=100)
    marks=forms.IntegerField()
    rollno=forms.IntegerField()
    def clean_name(self):
        print('Validating name field')
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("Name's characters should be at least 4.")
        return inputname
    def clean_rollno(self):
        print('Validating name field')
        inputrollno=self.cleaned_data['rollno']
        return inputrollno

