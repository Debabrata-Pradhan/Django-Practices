from django import forms
class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    def clean(self):
        print("Validating Total Form....")
        total_cleaned_data=super().clean()
        print("Validating Name")
        inputname=total_cleaned_data['name']
        if inputname[0].lower()!='s':
            raise forms.ValidationError("Name Should Start with 'S")
        print("Validating Rollno")
        inputrollno=total_cleaned_data['rollno']
        if inputrollno<=0:
            raise forms.ValidationError("Invalid Roll No.")
        print("Validating Email")
        inputemail=total_cleaned_data['email']
        if inputemail[-10:]!='@gmail.com':
            raise forms.ValidationError("Email Extension should be gmail.com")


