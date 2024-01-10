from django import forms
from django.core import validators



class studentForm(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField(validators=[validators.MinLengthValidator(5)])
    DOB=forms.DateField()
    email=forms.EmailField(required=True)
    re_enter=forms.EmailField(required=True)
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('Invalid Data')

    