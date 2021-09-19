from main_app.models import Provider
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Provider, Vaccine



# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def providers_index(request):
    providers = Provider.objects.all()
    return render(request, 'providers/index.html', { 'providers': providers })

def providers_detail(request, provider_id):
    try:
        provider = Provider.objects.get(id=provider_id)
        vaccines_provider_doesnt_have = Vaccine.objects.exclude(id__in = provider.vaccines.all().values_list('id'))
        return render(request, 'providers/detail.html', { 'provider': provider, 'vaccines': vaccines_provider_doesnt_have })
    except(Provider.DoesNotExist):
        return redirect('/providers')

class ProviderCreate(CreateView):
    model = Provider
    fields = ['name', 'address', 'phone', 'appointment', 'walkin', 'hours']

class ProviderUpdate(UpdateView):
    model = Provider
    fields = ['address', 'phone', 'appointment', 'walkin', 'hours']

class ProviderDelete(DeleteView):
    model = Provider
    success_url = '/providers/'

def assoc_vaccine(request, provider_id, vaccine_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Provider.objects.get(id=provider_id).vaccines.add(vaccine_id)
  return redirect('detail', provider_id=provider_id)