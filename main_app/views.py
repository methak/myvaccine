from main_app.models import Provider
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Provider


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def providers_index(request):
    providers = Provider.objects.all()
    return render(request, 'providers/index.html', { 'providers': providers })

def providers_detail(request, provider_id):
    provider = Provider.objects.get(id=provider_id)
    return render(request, 'providers/detail.html', { 'provider': provider })

class ProviderCreate(CreateView):
    model = Provider
    fields = ['name', 'address', 'phone', 'appointment', 'walkin', 'hours']

class ProviderUpdate(UpdateView):
    model = Provider
    fields = ['address', 'phone', 'hours']

class ProviderDelete(DeleteView):
    model = Provider
    success_url = '/providers/'
