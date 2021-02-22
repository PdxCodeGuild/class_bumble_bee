

from django.urls import path

from . import views


app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_contacts/', views.get_contacts, name='get_contacts'),
]




