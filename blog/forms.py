from django import forms
from .models import Category, Comment
class SimpleForm(forms.Form):
    # specify fields to be displayed.

    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields= '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model= Comment
        fields= '__all__'



            
   
