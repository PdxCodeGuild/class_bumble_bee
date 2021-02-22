from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact

def index(request):
    return render(request, 'contacts/index.html', {})

def get_contacts(request):
    # return JsonResponse({'a': 1, 'b': 2})
    
    # get all the contacts out of the database
    contacts = Contact.objects.all()
    # turning our queryset of contacts into a list of dictionaries
    # json can only contain: null, boolean, string, number, lists, objects
    contact_data = []
    for contact in contacts:
        contact_data.append({
            'name': contact.name,
            'age': contact.age,
            'image': contact.image.url if contact.image else '',
        })
    print(contact_data)
    return JsonResponse({'contacts': contact_data})

