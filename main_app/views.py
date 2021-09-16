from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def providers_index(request):
  return render(request, 'providers/index.html', { 'providers': providers })

class Provider:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

providers = [
  Provider('Lolo', 'tabby', 'foul little demon', 3),
  Provider('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Provider('Raven', 'black tripod', '3 legged cat', 4)
]