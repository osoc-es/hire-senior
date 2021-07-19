from django import forms
from typing import *
from validate_email import validate_email
import phonenumbers
from pygeocoder import Geocoder

def validate_address(country: str, street: str, st_number: int, city: str) -> bool:
	correct: bool = True
	#now we must see if the inputed values are correct	
	#we create the address
	address = street + ' ' + str(st_number) +  ' ' + city + ' ' + country
	address_geocode = Geocoder('AIzaSyAZSLXWoyAC5A2sNf5dyn_nSrHwBJCX8Sc').geocode(address)
	if not address_geocode.valid_address:
		correct = False
	return correct	

def validate_emails(email: str) -> bool:
	correct: bool = True
	#check if email is correct
	is_valid_email = validate_email(email_address = email, check_format = True, check_blacklist = True, check_dns = True, check_smtp = True)
	if not is_valid_email:
				correct = False
	return correct					

def validate_number(mobile_number: int) -> bool:
	correct: bool = True
	#check if number is correct
	number_parsed = phonenumbers.parse('+' + mobile_number)
	if not phonenumbers.is_valid_number(number_parsed):
		correct = False		
	return correct		

class UserForm(forms.Form):
	name = forms.CharField(label = 'first_name', max_length = 30)
	last_name1 = forms.CharField(label ='last_name1', max_length = 30)
	last_name2 = forms.CharField(label = 'last_name2', max_length = 30)
	mobile_number = forms.CharField(label ='mobile_number', max_length = 30)
	email = forms.CharField(label = 'email', max_length = 30)
	username = forms.CharField(label ='username', max_length = 30)
	password = forms.CharField(label = 'password', max_length = 30)
	age = forms.IntegerField(label= 'age')
	country = forms.CharField(label ='country', max_length = 30)
	street = forms.CharField(label = 'street', max_length = 60)
	st_number = forms.IntegerField(label ='st_number')
	city = forms.CharField(label ='city', max_length = 30)
	postal_code = forms.IntegerField(label = 'postal_code')
	#company = forms.CharField(label = 'company', max_length = 30)
	#position = forms.CharField(label ='job_position', max_length = 30)
	#period = forms.CharField(label = 'duration', max_length = 30)
	#job_description = forms.CharField(label = 'job_description', widget = forms.Textarea, max_length = 100)

	def clean(self):
		#here we define how to verify the data entered
		cleaned_data = super().clean()

		#LOCATION
		country = self.cleaned_data.get('country')
		street = self.cleaned_data.get('street')
		st_number = self.cleaned_data.get('st_number')
		city = self.cleaned_data.get('city')

		if country and street and st_number and city:
			if not validate_address(country, street, st_number, city):
				raise forms.ValidationError('Invalid Home Address')

		#EMAIL
		email = self.cleaned_data.get('email')

		if email:
			if not validate_emails(email):
				raise forms.ValidationError('Invalid Email Address')

		#PHONE NUMBER
		mobile_number = self.cleaned_data.get('mobile_number')

		if mobile_number:
			if not validate_number(mobile_number):
				raise forms.ValidationError('Invalid Phone Number')



class CompanyForm(forms.Form):
	name = forms.CharField(label = 'first_name', max_length = 30)
	password = forms.CharField(label = 'password', max_length = 30)
	description = forms.CharField(label = 'description', widget = forms.Textarea, max_length = 100)
	sector = forms.CharField(label = 'sector', max_length = 30)
	country = forms.CharField(label ='country', max_length = 30)
	street = forms.CharField(label = 'street', max_length = 60)
	st_number = forms.IntegerField(label ='st_number')
	city = forms.CharField(label ='city', max_length = 30)
	no_employees = forms.IntegerField(label = 'no_employees')
	website = forms.URLField(label = 'website')

	def clean(self):
		#here we define how to verify the data entered
		cleaned_data = super().clean()

		#LOCATION
		country = self.cleaned_data.get('country')
		street = self.cleaned_data.get('street')
		st_number = self.cleaned_data.get('st_number')
		city = self.cleaned_data.get('city')

		if country and street and st_number and city:
			if not validate_address(country, street, st_number, city):
				raise forms.ValidationError('Invalid Company Location') 


class CompanyEdit1(forms.Form):
	company_name = forms.CharField(label = 'company_name', max_length = 30)
	description = forms.CharField(label = 'description', widget = forms.Textarea, max_length = 100)
	sector = forms.CharField(label = 'sector', max_length = 30)


class CompanyEdit2(forms.Form):
	old_password = forms.CharField(label = 'old_password', max_length = 30)
	new_password = forms.CharField(label = 'new_password', max_length = 30)
	new_password2 = forms.CharField(label = 'new_password2', max_length = 30)


class CompanyEdit3(forms.Form):
	description = forms.CharField(label = 'description', widget = forms.Textarea, max_length = 100)
	country = forms.CharField(label ='country', max_length = 30)
	street = forms.CharField(label = 'street', max_length = 30)
	st_number = forms.IntegerField(label ='st_number')
	city = forms.CharField(label ='city', max_length = 30)
	no_employees = forms.IntegerField(label = 'no_employees')
	website = forms.URLField(label = 'website')	

	def clean(self):
		#here we define how to verify the data entered
		cleaned_data = super().clean()

		#LOCATION
		country = self.cleaned_data.get('country')
		street = self.cleaned_data.get('street')
		st_number = self.cleaned_data.get('st_number')
		city = self.cleaned_data.get('city')

		if country and street and st_number and city:
			if not validate_address(country, street, st_number, city):
				raise forms.ValidationError('Invalid Company Location') 

class UserEdit1(forms.Form):
	username = forms.CharField(label ='username', max_length = 30)
	name = forms.CharField(label = 'name', max_length = 30)
	last_name1 = forms.CharField(label ='last_name1', max_length = 30)
	last_name2 = forms.CharField(label = 'last_name2', max_length = 30)
	email = forms.CharField(label = 'email', max_length = 30)
	mobile_number = forms.CharField(label ='mobile_number', max_length = 30)

	def clean(self):
		#here we define how to verify the data entered
		cleaned_data = super().clean()

		#EMAIL
		email = self.cleaned_data.get('email')

		if email:
			if not validate_emails(email):
				raise forms.ValidationError('Invalid Email Address')

		#PHONE NUMBER
		mobile_number = self.cleaned_data.get('mobile_number')

		if mobile_number:
			if not validate_number(mobile_number):
				raise forms.ValidationError('Invalid Phone Number')

class UserEdit2(forms.Form):
	old_password = forms.CharField(label = 'old_password', max_length = 30)
	new_password = forms.CharField(label = 'new_password', max_length = 30)
	new_password2 = forms.CharField(label = 'new_password2', max_length = 30)


class UserEdit3(forms.Form):
	age = forms.IntegerField(label= 'age')
	country = forms.CharField(label ='country', max_length = 30)
	street = forms.CharField(label = 'street', max_length = 30)
	st_number = forms.IntegerField(label ='st_number')
	city = forms.CharField(label ='city', max_length = 30)
	postal_code = forms.IntegerField(label = 'postal_code')
	
	def clean(self):
		#here we define how to verify the data entered
		cleaned_data = super().clean()

		#LOCATION
		country = self.cleaned_data.get('country')
		street = self.cleaned_data.get('street')
		st_number = self.cleaned_data.get('st_number')
		city = self.cleaned_data.get('city')

		if country and street and st_number and city:
			if not validate_address(country, street, st_number, city):
				raise forms.ValidationError('Invalid Company Location') 				