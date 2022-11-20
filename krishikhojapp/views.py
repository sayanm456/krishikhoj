from django.shortcuts import render, redirect
from .forms import FarmerForm
from .models import Farmer
# from django.http import HttpResponse

def farmer_form(request):
    if request.method == "GET":
        form = FarmerForm()
        return render(request, 'krishikhojapp/farmer_form.html',{'form': form})
    else:
        form = FarmerForm(request.POST)  
        if form.is_valid():
           form.save()
        return redirect('/krishikhojapp/list/')    

def tractor_list(request):
    context = {'tractor_list': Farmer.objects.all()}
    return render(request, 'krishikhojapp/tractor_list.html', context)