from django import forms

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

from myapp.models import comment

class commentForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=('name','email','body')

