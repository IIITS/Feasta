from django import forms
from django.contrib.auth.forms import *
from feasta.config import model_choices
class LoginForm(AuthenticationForm):
	username = forms.CharField(
		widget=forms.TextInput(
		attrs={
			'class':'form-control',
			'id':'username',
			'placeholder':'Enter your username or email'
			}
		))
	password = forms.CharField(
		widget=forms.PasswordInput(
		attrs={
			'class':'form-control',
			'id':'password',
			'placeholder':'Enter your password'
			}
		))
	

class UnregisterForm(forms.Form):
	meal = forms.CharField(
			widget=forms.Select(choices=model_choices['MEAL'],
			attrs={
				'class':'form-control feasta-blackfont',
			}
		))

	date = forms.DateField(
		widget=forms.DateInput(
			attrs={
			    'class':'form-control'
			}
		))
class BulkUnregisterForm(forms.Form):
	start_date = forms.DateField(widget=forms.DateInput(
			attrs={
			    'class':'form-control'
			}
		))
	start_meal = forms.CharField(
			widget=forms.Select(choices=model_choices['MEAL'],
			attrs={
				'class':'form-control feasta-blackfont',
			}
		))
	end_date = forms.DateField(widget=forms.DateInput(
			attrs={
			    'class':'form-control'
			}
		))
	end_meal = forms.CharField(
			widget=forms.Select(choices=model_choices['MEAL'],
			attrs={
				'class':'form-control feasta-blackfont',
			}
		))
