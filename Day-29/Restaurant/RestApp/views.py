from django.shortcuts import render
from django.http import HttpResponse
from RestApp.forms import ReForm
# Create your views here.


def home(r):
	return render(r,'app/home.html')
def about(r):
	return render(r,'app/about.html')
def contact(r):
	return render(r,'app/contact.html')

def login(r):
	return render(r,'app/login.html')


def restlist(r):
	t=ReForm()
	return render(r,'app/restaurantlist.html',{'q':t})















