from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Provider, Vaccine, VaccineCard
from main_app.forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@login_required
def home(request):
    vac_cards = VaccineCard.objects.filter(user=request.user)

    return render(request, 'home.html', {'vac_cards': vac_cards})
    

def about(request):
    return render(request, 'about.html')

@login_required
def providers_index(request):
    providers = Provider.objects.all()
    return render(request, 'providers/index.html', { 'providers': providers })

@login_required
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

@login_required
def assoc_vaccine(request, provider_id, vaccine_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Provider.objects.get(id=provider_id).vaccines.add(vaccine_id)
  return redirect('detail', provider_id=provider_id)

@login_required
def book_vaccine(request, provider_id, vaccine_id):
    u=request.user
    print(u)
    p=Provider.objects.get(id=provider_id)
    print(p)
    v=Vaccine.objects.get(id=vaccine_id)
    print(v)
    vaccine_card= VaccineCard(user=u, provider=p, vaccine=v)
    vaccine_card.save()
    
    return redirect('home',)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    
    form = UserForm()
    context = {'form': form, 'error_message': error_message}

    return render(request, 'registration/signup.html', context)