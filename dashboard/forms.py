from django import forms
from .models import imagerequest, bugs

class graphForm(forms.Form):
    associatie = forms.BooleanField(required=False, label='Associatie')
    onder_kenm = forms.BooleanField(required=False, label='Onderscheidend Kenmerk')
    filter_term = forms.CharField(required=False)
    ok = forms.ChoiceField(choices=[('OBJECT', 'OBJECT'), ('DIGITALE COLLECTIE', 'DIGITALE COLLECTIE'), ('DOCUMENTAIRE COLLECTIE', 'DOCUMENTAIRE COLLECTIE'), ('BEELD', 'BEELD'), ('TEXTIEL', 'TEXTIEL'), ('AUDIOVISUELE COLLECTIE', 'AUDIOVISUELE COLLECTIE')])

class checkForm(forms.Form):
    association = forms.BooleanField(required=False, label='Association')
    full_collection = forms.BooleanField(required=False, label='Entire Collection')
    filterterm = forms.CharField(required=False)

class rschijfForm(forms.Form):
    objectnumber = forms.CharField(required=False, label='Objectnummer')

class Imageform(forms.ModelForm):
    class Meta:
        model = imagerequest
        fields = '__all__'

class Bugsform(forms.ModelForm):
    class Meta:
        model = bugs
        fields = '__all__'

