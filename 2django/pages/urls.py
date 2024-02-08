from django.urls import path
from .views import homePageView
# By using the period .views we reference the current directory, which is our pages app containing both views.py and urls.py

urlpatterns = [
    path('', homePageView, name='home')
]

# • a Python regular expression for the empty string ''
# • specify the view which is called homePageView
# • add an optional URL name of 'home'