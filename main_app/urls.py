from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('providers/', views.providers_index, name='index'),
    path('providers/<int:provider_id>/', views.providers_detail, name='detail'),
    path('providers/create/', views.ProviderCreate.as_view(), name='providers_create'),
    path('providers/<int:pk>/update/', views.ProviderUpdate.as_view(), name='providers_update'),
    path('providers/<int:pk>/delete/', views.ProviderDelete.as_view(), name='providers_delete'),
 
    path('providers/<int:provider_id>/assoc_vaccine/<int:vaccine_id>/', views.assoc_vaccine, name='assoc_vaccine'),  

    path('providers/<int:provider_id>/book_vaccine/<int:vaccine_id>/', views.book_vaccine, name='book_vaccine'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),  
]