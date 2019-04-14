from django.test import Client,TestCase
from django.contrib.auth.models import User

class urltestcase1(TestCase):
    def test_categorypage(self):
        self.client=Client()
        response = self.client.get('/myappcategory')
        self.assertEqual(response.status_code, 200)
    def test_categorypageinvalid(self):
       self.client=Client()
       response = self.client.get('myapp/oops')
       self.assertEqual(response.status_code, 404)


# Create your tests here.
