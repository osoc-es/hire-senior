from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import *
from pygeocoder import Geocoder

# Create your views here.
#if we recieve a request to go to the index page it will redirect here and return the value specified
#to call this view we have to configure it in the URLconfig
def index(request):
	template = loader.get_template('app1/index.html')
	return HttpResponse(template.render({}, request))

def register_user(request, user_registered: bool = False):
	#if the user has entered the data and pressed submit it will create a post and we will get the info from the form
	if request.method == 'POST':
		form = UserForm(request.POST)
		#form is valid is to prevent for attacks like SQL injections
		if form.is_valid(): 
			#we start by saying the form is correct and later check conditions
			correct: bool = True

			#getting all the clean data
			first_name = form.cleaned_data.get('nombre')
			last_names= form.cleaned_data.get('apellidos')		
			country = form.cleaned_data.get('pais')
			street = form.cleaned_data.get('calle')
			st_number = form.cleaned_data.get('numero')
			city = form.cleaned_data.get('ciudad')
			#cv = form.cleaned_data.get('archivo')
			job_position = form.cleaned_data.get('tipo de posicion')
			company = form.cleaned_data.get('empresa')
			duration = form.cleaned_data.get('duracion')
			education = form.cleaned_data.get('educacion')
			volunteer_work = form.cleaned_data.get('voluntariado')

	#if it is any other method rather than post, form will be in original state		
	else:
		form = UserForm()	
	
	template = loader.get_template('app1/register_user.html')
	context = {'form': form}
	return HttpResponse(template.render(context, request))