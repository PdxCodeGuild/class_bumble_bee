

from django.urls import path

from . import views


app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_contacts/', views.get_contacts, name='get_contacts'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('create_contact2/', views.create_contact2, name='create_contact2'),
]




