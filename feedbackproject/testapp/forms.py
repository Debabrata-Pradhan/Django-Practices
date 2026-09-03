from django import forms
class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    def clean_name(self):
        print("Validating name field...")
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("The minimum number of character for the name should be 4")
        return inputname
    def clean_rollno(self):
        print("Validating Rollno field...")
        inputrollno=self.cleaned_data['rollno']
        if inputrollno<0:
            raise forms.ValidationError("Roll no should be above 0")
        return inputrollno
    def clean_email(self):
        print("Validating Email field...")
        inputemail=self.cleaned_data['email']
        return inputemail
    def clean_feedback(self):
        print("Validating Feedback field...")
        inputfeedback=self.cleaned_data['feedback']
        return inputfeedback