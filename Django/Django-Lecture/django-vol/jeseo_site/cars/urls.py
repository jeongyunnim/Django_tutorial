from django.urls import path
from . import views

# template에서 url 태그를 사용하기 위해 app 이름을 지정
app_name = 'cars'

urlpatterns = [
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('test/', views.test, name='test'),
]