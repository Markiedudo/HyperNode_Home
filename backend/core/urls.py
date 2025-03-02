from django.urls import path
from . import views
from .views import test_translation
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('test-translation/', test_translation, name='test_translation'),  # Debug route

]