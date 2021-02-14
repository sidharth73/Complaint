from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fir

# Create your views here.
def sid(request):
	return render(request, "online/sid.html")

def registered(request):
	print("Form Submitted.")
	name = request.POST["name"]
	address = request.POST["address"]
	complaint = request.POST["complaint"]

	fir = Fir(name=name, address=address, complaint=complaint)
	fir.save()
	return render(request, "online/registered.html")