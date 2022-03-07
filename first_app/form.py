from django import forms
from django.core import validators
from first_app.models import User


def check_name(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name need to start with z')


class MyForm(forms.Form):
    name = forms.CharField(validators=[check_name])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Re-Enter Your Email')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, 
                                 widget=forms.HiddenInput, validators=[
                                 validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError('message')

class MyForm_Modal(forms.ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'