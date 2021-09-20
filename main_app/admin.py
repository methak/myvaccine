from django.contrib import admin
from .models import Provider, Vaccine, VaccineCard

admin.site.register(Provider)
admin.site.register(Vaccine)
admin.site.register(VaccineCard)
