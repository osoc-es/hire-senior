from django.db import models

# Create your models here.

#create tables in the schema

class User(models.Model):
	#we define the columns with the various options
	#CharField and integerfield are some of the types of variables we can introduce into each column
	username = models.CharField(max_length = 45, db_column = 'username', unique = True, null = True) #we must make sure that the usernames are all unique
	user_password = models.CharField(max_length = 45, db_column = 'password', null = True)
	user_name = models.CharField(max_length = 45, db_column = 'name', null = True)
	last_name1 = models.CharField(max_length = 45, db_column = 'last_name1', null = True)
	last_name2 = models.CharField(max_length = 45,db_column = 'last_name2', null = True)
	user_age = models.IntegerField(db_column = 'age', null = True)
	user_email = models.CharField(max_length = 45, db_column = 'email', null = True)
	user_number = models.BigIntegerField(db_column = 'mobile_number', null = True)
	user_country = models.CharField(max_length = 45, db_column = 'country', null = True)
	user_street = models.CharField(max_length = 45, db_column = 'street', null = True)
	user_st_number = models.IntegerField(db_column = 'number', null = True)
	user_city = models.CharField(max_length = 45, db_column = 'city', null = True)
	user_postal_code = models.IntegerField(db_column = 'postal_code', null = True)
	#user_CV = models.TextField(db_column = 'cv', null = True)
	#user_job_position = models.CharField(max_length = 45, db_column = 'job_position', null = True) #we must make sure that the usernames are all unique
	#user_company = models.CharField(max_length = 45, db_column = 'company', null = True)
	#user_job_duration = models.CharField(max_length = 45, db_column = 'duration', null = True) #we must make sure that the usernames are all unique
	#user_job_description = models.CharField(max_length = 250, db_column = 'job_description', null = True)
	user_date_registered = models.DateTimeField(db_column = 'date_registered', null = True)
	#how to show the user when referenced
	def __str__(self):
		return f'{self.user_name} {self.last_name1} {self.last_name2} ({self.username})'

	#to edit the name of the table
	class Meta:
		db_table = 'user'


class Company(models.Model):
	#defining the columns with the various variables
	company_name = models.CharField(max_length = 45, db_column = 'name', null = True, unique = True)
	company_password = models.CharField(max_length = 45, db_column = 'password', null = True)
	company_description = models.TextField(db_column = 'description', null = True)
	company_sector = models.CharField(max_length = 45, db_column = 'sector', null = True)
	company_country = models.CharField(max_length = 45, db_column = 'country', null = True)
	company_street = models.CharField(max_length = 45, db_column = 'street', null = True)
	company_city = models.CharField(max_length = 45, db_column = 'city', null = True)
	company_st_number = models.IntegerField(db_column = 'number', null = True)
	n_employees = models.IntegerField(db_column = 'number_of_employees', null = True)
	company_website = models.URLField(max_length = 200, db_column = 'website', null = True)
	company_date_registered = models.DateTimeField(db_column = 'date_registered', null = True)

	def __str__(self):
		return self.company_name


	#to edit the name of the table
	class Meta:
		db_table = 'company'

class Work_Experience(models.Model):
	#defining the columns with the various variables
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	username = models.CharField(max_length = 45, db_column = 'username', null = True)
	job_title = models.CharField(max_length = 45, db_column = 'job_title', null = True)
	company = models.CharField(max_length = 45, db_column = 'company', null = True)
	duration = models.FloatField(db_column = 'duration_years', null = True)

	def __str__(self):
		return self.job_title + 'at' + self.company

	class Meta:
		db_table = 'work_experience'

class Job(models.Model):
	#defining the columns with the various variables
	company = models.ForeignKey(Company, on_delete = models.CASCADE)
	company_name = models.CharField(max_length = 45, db_column = 'company_names', null = True)
	job_title = models.CharField(max_length = 45, db_column = 'job_title', null = True)
	job_description = models.TextField(db_column = 'job_description', null = True)

	def __str__(self):
		return self.job_title + 'at' + self.company_name

	class Meta:
		db_table = 'job'	




