from django.urls import path
from . import views

#aqui ponemos los diferentes urls a los que se puede acceder dentro de la app de polls
urlpatterns = [
			path('', views.index, name = 'index'),
			path('register/user/', views.register_user, name = 'register_user'), 
			path('register/company/', views.register_company, name = 'register_company'),
			path('user/<str:username>/profile/', views.profile_user, name = 'user_profile'),
			path('company/<str:name>/profile/', views.profile_company, name = 'company_profile'),
			path('company/<str:name>/home/', views.home_company, name = 'company_home'),
			path('user/<str:username>/home/', views.home_user, name = 'user_home'),
			path('company/<str:name>/add-job', views.add_job, name = 'add_job'),
			path('company/<str:name>/search-users', views.search_user, name = 'search_user')
]
