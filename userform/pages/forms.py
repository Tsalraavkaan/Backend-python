from django import forms
 
class UserForm(forms.Form):
    surname = forms.CharField()
    name = forms.CharField()
    age = forms.IntegerField()
    place_of_studying = forms.CharField()
    email = forms.EmailField()