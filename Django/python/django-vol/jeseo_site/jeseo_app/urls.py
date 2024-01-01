from django.urls import path
from . import views

urlpatterns = [
	# path('<int:num1>/<int:num2>', views.plus_view),
	path('<int:num>', views.news_num_view),
	path('<str:topic>/', views.news_view),
] 
