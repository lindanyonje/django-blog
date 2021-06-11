from django import forms

class SimpleForm(forms.Form):
    # specify fields to be displayed.

    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)