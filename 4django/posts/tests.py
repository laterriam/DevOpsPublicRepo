# posts/tests.py
from django.test import TestCase
# TestCase lets us create a sample database
from django.urls import reverse # let's us test our view
from .models import Post

# Create your tests here.
# Test our Model
class PostModelTest(TestCase):
    # setUp methods are not actually test but they enable us to run the 
    # subsequent tests
    def setUp(self):
        Post.objects.create(text='sample text: object was created')
    # new class PostModelTest and add a method setUp to create a 
    # new database that has just one entry: a post with a text field 
    # containing the string 'object was created'
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'sample text: object was created')
        # Here we run our firt test called "test_text_content" to check that the
        # database field actually contains a "test". We created a variable called
        # "post" that respresents the first id on our Post Model. If we created
        # another entry for our test Django will automatically give an id = 2
        # f strings let us put variables directly in our strings with the {} brackets.
        # Here we are setting expected_object_name to be the string of 
        # the value in post.text (which is "object was created").

# To run our test:
# python manage.py test

# Test our Homepage: checking the pattern Template > View > URLs
class HomePageViewTest(TestCase):
    # setUp methods are not actually test but they enable us to run the 
    # subsequent tests
    def setUp(self):
        Post.objects.create(text="creating another object for testing")
    
    # Testing whether our view exists by URL
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    # Testing whether our view exists by name
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    # Testing whether our template was applied to create the view
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
    

    