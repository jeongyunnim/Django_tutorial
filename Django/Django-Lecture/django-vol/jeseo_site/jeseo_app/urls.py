from django.urls import path
from . import views

#register the app namespace
app_name = 'jeseo_app'

urlpatterns = [
	path('', views.example_view, name='example'),
	path('variable/', views.variable_view, name='variable'),
] 
