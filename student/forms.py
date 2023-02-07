from django import forms

class studentForm(forms.Form):
    nim = forms.IntegerField()
    name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    phone = forms.IntegerField()