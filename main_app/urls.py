from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('providers/', views.providers_index, name='index'),
    path('providers/<int:provider_id>/', views.providers_detail, name='detail'),
    path('providers/create/', views.ProviderCreate.as_view(), name='providers_create'),
    path('providers/<int:pk>/update/', views.ProviderUpdate.as_view(), name='providers_update'),
    path('providers/<int:pk>/delete/', views.ProviderDelete.as_view(), name='providers_delete'),   
]