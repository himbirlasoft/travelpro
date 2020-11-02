from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Destination

# Create your views here.
def index(request):
    dest1= Destination()
    dest1.name='Mumbai'
    dest1.desc='Mumbai is the bese place'
    dest1.price=1100
    dest1.img='destination_1.jpg'

    dest2= Destination()
    dest2.name='Delhi'
    dest2.desc='Delhi is the bese place'
    dest2.price=1100
    dest2.img='destination_2.jpg'

    dest3= Destination()
    dest3.name='Kanpur'
    dest3.desc='Kanpur is the bese place'
    dest3.price=1100
    dest3.img='destination_3.jpg'

    dest=[dest1,dest2,dest3]

    return render(request,"index.html",{'dest':dest} )