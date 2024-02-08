# posts/views.py
from django.views.generic import ListView
from .models import Post
# Internally in Django ListView returns an object called object_list 
# that we want to display in our template.

# Create your views here.
class HomePageView(ListView):
    model = Post # extract data from our model
    template_name = 'home.html' # associate a template to be used with this view
    context_object_name = 'all_posts_list' # template's object_list a specific name
