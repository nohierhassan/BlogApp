from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import ExtendedUser


class RegistrationForm(UserCreationForm):
	# we will use a predefined form in django to check for us the fields
	# the unique constraints will be checked in the ExtendedUser itself
	email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

	class Meta:
		model = ExtendedUser
		#fields to be shown in the form
		fields = ("email", "username", "password1", "password2")
		
class LoginForm(forms.ModelForm):
	# we will modify in the model forms our own login form as we already overriden the django User Model
	password = forms.CharField(label = 'Password', widget = forms.PasswordInput)

	class Meta:
		model = ExtendedUser
		#fields to be shown in the form
		fields = ('email','password')

	# to validate the login before submission
	def clean(self):
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']
		if not authenticate(email = email, password = password):
			raise forms.ValidationError("Invalid Username or Password")




