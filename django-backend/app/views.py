from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import *
from .models import *
from datetime import datetime

# Create your views here.
#if we recieve a request to go to the index page it will redirect here and return the value specified
#to call this view we have to configure it in the URLconfig
def index(request):
	template = loader.get_template('app1/index.html')
	return HttpResponse(template.render({}, request))

def register_user(request):
	#if the user has entered the data and pressed submit it will create a post and we will get the info from the form
	if request.method == 'POST':
		form = UserForm(request.POST)
		#form is valid is to prevent for attacks like SQL injections
		if form.is_valid(): 
			#we start by saying the form is correct and later check conditions
			correct: bool = True

			#getting all the clean data
			first_name = form.cleaned_data.get('name')
			last_name1= form.cleaned_data.get('last_name1')	
			last_name2 = form.cleaned_data.get('last_name2')
			mobile_number = form.cleaned_data.get('mobile_number')
			email = form.cleaned_data.get('email')
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			age = form.cleaned_data.get('age')	
			country = form.cleaned_data.get('country')
			street = form.cleaned_data.get('street')
			st_number = form.cleaned_data.get('st_number')
			city = form.cleaned_data.get('city')
			postal_code = form.cleaned_data.get('postal_code')
			#cv = form.cleaned_data.get('archivo')
			#job_position = form.cleaned_data.get('position')
			#company = form.cleaned_data.get('company')
			#duration = form.cleaned_data.get('period')
			#job_description = form.cleaned_data.get('job_description')
	
			objective: str = ''
			#we obtain the values of the checkbox
			if 'objective1' in request.POST:
				objective += 'Continuar desarrollándome en el sector, '
			if 'objective2' in request.POST:
				objective += 'Aportar mi experiencia a gente en formación, '
			if 'objective3' in request.POST:
				objective += 'Ayudar a integrarse a nuevos trabajadores, '
			if 'objective4' in request.POST:
				objective += 'Otra opción'			

			#we will create a user instance and add to database
			u = User(username = username, user_password = password, user_name = first_name, last_name1 = last_name1, last_name2 = last_name2, user_age = age, user_email = email, user_number = mobile_number, user_country = country, user_street = street, user_st_number = st_number, user_postal_code = postal_code, user_date_registered = datetime.now())					
			#user_job_position = job_position, user_company = company, user_job_duration = duration, user_job_description = job_description,
			u.save()

			#redirect to users profile page
			return HttpResponseRedirect(f'/user/{username}/home/')

	#if it is any other method rather than post, form will be in original state		
	else:
		form = UserForm()	

	template = loader.get_template('app1/register_user.html')
	context = {'form': form}
	return HttpResponse(template.render(context, request))	

def register_company(request):
	#if the user has entered the data and pressed submit it will create a post and we will get the info from the form
	if request.method == 'POST':
		form = CompanyForm(request.POST)

		#form is valid is to prevent for attacks like SQL injections
		if form.is_valid(): 
			#we start by saying the form is correct and later check conditions
			print(1)
			
			#getting all the clean data
			name = form.cleaned_data.get('name')
			password = form.cleaned_data.get('password')
			description = form.cleaned_data.get('description')
			sector = form.cleaned_data.get('sector')
			country = form.cleaned_data.get('country')
			street = form.cleaned_data.get('street')
			st_number = form.cleaned_data.get('st_number')
			city = form.cleaned_data.get('city')
			no_employees = form.cleaned_data.get('no_employees')
			website = form.cleaned_data.get('website')		

			#we will create a user instance and add to database
			c = Company(company_name = name, company_password = password, company_country = country, company_street = street, company_st_number = st_number, company_description = description, company_sector = sector, n_employees = no_employees, company_website = website, company_date_registered = datetime.now())					
			c.save()

			#redirect to users profile page
			return HttpResponseRedirect(f'/company/{name}/home/')	
			
	
	#if it is any other method rather than post, form will be in original state		
	else:
		form = UserForm()	

	context = {'form': form}
	template = loader.get_template('app1/register_company.html')
	return HttpResponse(template.render(context, request))

def profile_company(request, name: str):
	#first we get all the data from the database to be able to display it
	company = Company.objects.filter(company_name = name)
	company_values = company.values_list()[0]

	company_name_ = company_values[1]
	company_password = company_values[2]
	company_description = company_values[3]
	company_sector = company_values[4]
	company_country = company_values[5]
	company_street = company_values[6]
	company_st_number = company_values[7]
	company_city = company_values[8]
	company_website = company_values[10]
	company_no_employees = company_values[9]

	context = {'name': company_name_, 'description': company_description, 'sector': company_sector, 'country': company_country, 'street': company_street, 'st_number': company_st_number, 'city': company_city, 'no_employees': company_no_employees, 'website': company_website}

	#if the user has entered the data and pressed submit it will create a post and we will get the info from the form
	if request.method == 'POST' and 'b1' in request.POST:
		form = CompanyEdit1(request.POST)
		context['form'] = form
		if form.is_valid():
			#getting all the clean data
			company_name = form.cleaned_data.get('company_name')
			description = form.cleaned_data.get('description')
			sector = form.cleaned_data.get('sector')
			company.update(company_name = company_name, company_description = description, company_sector = sector)

			return HttpResponseRedirect(f'/company/{company_name}/profile')

	#if the user has entered the data and pressed submit it will create a post and we will get the info from the form
	"""
	if request.method == 'POST' and 'b2' in request.POST:
		form = CompanyEdit2(request.POST)
		if form.is_valid():
			#getting all the clean data
	"""	
	#if the user has entered the data and pressed submit it will create a post and we will get the info from the form
	if request.method == 'POST' and 'b3' in request.POST:
		form = CompanyEdit3(request.POST)
		context['form'] = form
		if form.is_valid():
			#getting all the cleaned data
			description = form.cleaned_data.get('description')
			country = form.cleaned_data.get('country')
			street = form.cleaned_data.get('street')
			st_number = form.cleaned_data.get('st_number')
			city = form.cleaned_data.get('city')
			no_employees = form.cleaned_data.get('no_employees')
			website = form.cleaned_data.get('website')

			company.update(company_description = description, company_country = country, company_street = street, company_st_number = st_number, company_city = city, company_no_employees = no_employees, company_website = website)
			return HttpResponseRedirect(f'/company/{name}/profile')

	template = loader.get_template('app1/profile_company.html')
	return HttpResponse(template.render(context, request))

def profile_user(request, username: str):
	#first we get all the data from the database to be able to display it
	user = User.objects.filter(username = username)
	user_values = user.values_list()[0]

	username_ = user_values[1]
	user_password = user_values[2]
	user_name = user_values[3]
	user_last_name1 = user_values[4]
	user_last_name2 = user_values[5]
	user_age = user_values[6]
	user_email = user_values[7]
	user_number = user_values[8]
	user_country = user_values[9]
	user_street = user_values[10]
	user_st_number = user_values[11]
	user_city = user_values[12]
	user_postal_code = user_values[13]

	context = {'mobile_number': user_number, 'age': user_age, 'email': user_email, 'postal_code': user_postal_code, 'name': user_name, 'username': username_, 'password': user_password, 'country': user_country, 'street': user_street, 'st_number': user_st_number, 'city': user_city, 'last_name1': user_last_name1, 'last_name2': user_last_name2}

	#if the user has entered the data and pressed submit it will create a post and we will get the info from the form
	if request.method == 'POST' and 'b1' in request.POST:
		form = UserEdit1(request.POST)
		context['form'] = form
		if form.is_valid():
			#getting all the clean data
			username = form.cleaned_data.get('username')
			name = form.cleaned_data.get('name')
			last_name1 = form.cleaned_data.get('last_name1')
			last_name2 = form.cleaned_data.get('last_name2')
			email = form.cleaned_data.get('email')
			mobile_number = form.cleaned_data.get('mobile_number')
			
			user.update(user_name = name, username = username, last_name1 = last_name1, last_name2 = last_name2, user_email = email, user_number = mobile_number)
			return HttpResponseRedirect(f'/user/{username}/profile')

	#if the user has entered the data and pressed submit it will create a post and we will get the info from the form
	"""
	if request.method == 'POST' and 'b2' in request.POST:
		form = CompanyEdit2(request.POST)
		if form.is_valid():
			#getting all the clean data
	"""	
	#if the user has entered the data and pressed submit it will create a post and we will get the info from the form
	if request.method == 'POST' and 'b3' in request.POST:
		form = UserEdit3(request.POST)
		context['form'] = form
		if form.is_valid():
			#getting all the cleaned data
			age = form.cleaned_data.get('age')
			country = form.cleaned_data.get('country')
			street = form.cleaned_data.get('street')
			st_number = form.cleaned_data.get('st_number')
			city = form.cleaned_data.get('city')
			postal_code = form.cleaned_data.get('postal_code')

			user.update(user_country = country, user_street = street, user_st_number = st_number, user_city = city, user_postal_code = postal_code)
			return HttpResponseRedirect(f'/user/{username_}/profile')

	template = loader.get_template('app1/profile_user.html')
	return HttpResponse(template.render(context, request))	

def home_company(request, name: str):
	context = {'name': name}
	template = loader.get_template('app1/home_company.html')
	return HttpResponse(template.render(context, request))	

def home_user(request, username: str):
	context = {'username': username}
	template = loader.get_template('app1/home_user.html')
	return HttpResponse(template.render(context, request))	

def add_job(request, name: str):
	context = {'name': name}
	template = loader.get_template('app1/index.html')
	return HttpResponse(template.render(context, request))	

def search_user(request, name: str):
	context = {'name': name}
	template = loader.get_template('app1/index.html')
	return HttpResponse(template.render(context, request))		
		


