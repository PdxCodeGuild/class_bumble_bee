from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from .models import Customer, City, State


def index(request):

    # dual class/table representation
    # the fields of the class are like the columns of the table
    # the instances of the class are like the rows of the table


    # get a record =====================================
    # get a row out of our table
    # the object that represents the row is an instance of the class in models.py
    city = City.objects.get(name='Portland')
    print(type(city))
    # city = City.objects.get(id=1)
    # city = City.objects.get(latitude=45.5051)
    print(city.name)
    print(city.latitude)
    print(city.longitude)

    # creating a new record ============================
    # oregon = State.objects.get(name='Oregon')
    # city = City(name='Salem', latitude=44.9429, longitude=-123.0351, state=oregon)
    # city.save()

    # updading a record ============================
    # city = City.objects.get(name='Salemm')
    # city.name = 'Salem'
    # city.save()

    oregon = State.objects.get(name='Oregon')
    print(oregon.name)
    print(type(oregon))

    cities = City.objects.all()
    for city in cities:
        print(city.name)
        print(type(city))
        print(city.state.name)
        print(type(city.state))
        # print(city.state_id)
        # print(city.latitude)
        # print(city.longitude)
        print()
    











    context = {
        'title': 'Hobby Lobby',
        'user': {
            'first_name': 'Jane',
            'last_name': 'Fonda',
            'age':6
        },
        'text_color': 'white',
        'paint_colors': ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponseRedirect('https://www.google.com/')

def contactus(request):
    return JsonResponse({'name': 'bob', 'age': 55})

def redirect(request):
    # http://localhost:8000/?name=bob&age=55
    print(request.GET)
    name = request.GET['name']
    age = request.GET['age']
    return HttpResponse('Hello ' + name + ' you are ' + age + ' years old')
    