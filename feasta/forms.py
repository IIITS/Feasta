from django import forms
from django.contrib.auth.forms import *
from feasta.config import model_choices
class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'mdl-textfield__input', 'id':'username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input', 'id':'password'}))
	

class UnregisterForm(forms.Form):
	meal = forms.CharField(
			widget=forms.Select(choices=model_choices['MEAL'],
			attrs={
				'class':'',
			}
		))

	date = forms.DateField(
		widget=forms.DateInput(
			attrs={
			    'class':''
			}
		))
class BulkUnregisterForm(forms.Form):
	start_date = forms.DateField()
	start_meal = forms.CharField(
			widget=forms.Select(choices=model_choices['MEAL'],
			attrs={
				'class':'',
			}
		))
	end_date = forms.DateField()
	end_meal = forms.CharField(
			widget=forms.Select(choices=model_choices['MEAL'],
			attrs={
				'class':'',
			}
		))
