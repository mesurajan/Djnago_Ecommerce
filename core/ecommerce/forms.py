from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)


class FeedbackForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(choices=[('1', '1 Star'), ('2', '2 Stars'), ('3', '3 Stars'), ('4', '4 Stars'), ('5', '5 Stars')])
    yes_no = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], widget=forms.RadioSelect)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
