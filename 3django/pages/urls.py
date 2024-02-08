# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, ContactusPageView
# By using the period .views we reference the current directory, which is our pages app containing both views.py and urls.py

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contactus/', ContactusPageView.as_view(), name='contactus'),
]

# • a Python regular expression for the empty string ''
# • specify the view which is called homePageView
# • add an optional URL name of 'home'