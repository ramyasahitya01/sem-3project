from django.test import Client,TestCase
from django.contrib.auth.models import User
from homepage.models import UserProfileInfo
from .models import *
from .forms import *
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
from finalapp.serializers import DocumentSerializer



from django.urls import reverse
class urltestcase1(TestCase):
    def setUp(self):
        self.createadmin=User.objects.create_user(username="test user",email="test@gmail.com",password="test password")
        self.client=None
        self.request_url='/finalapp/'
    def test_upload(self):
        self.client=Client()
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
    def test_uploadby_authenticated_user(self):
       self.client=Client()
       self.client.force_login(self.createadmin)
       response = self.client.get(self.request_url)
       self.assertEqual(response.status_code, 200)

    def test_upload_id(self):
       self.client=Client()
       response = self.client.get('finalapp/random')
       self.assertEqual(response.status_code, 404)

    def test_uploadby_authenticated_user_id(self):
      self.client=Client()
      self.client.force_login(self.createadmin)
      response = self.client.get('finalapp/randomm')
      self.assertEqual(response.status_code, 404)
class urltestcase2(TestCase):
    def setUp(self):
        self.createadmin=User.objects.create_user(username="test user",email="test@gmail.com",password="test password")
        self.client=None
        self.request_url='/finalapp/upload/'
    def test_formupload_image(self):
        self.client=Client()
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
    def test_formuploadby_authenticated_user(self):
       self.client=Client()
       self.client.force_login(self.createadmin)
       response = self.client.get(self.request_url)
       self.assertEqual(response.status_code, 200)
    def test_formuploadby_authenticated_user_id(self):
      self.client=Client()
      self.client.force_login(self.createadmin)
      response = self.client.get('finalapp/randommm')
      self.assertEqual(response.status_code, 404)
    def test_upload_image_invalid(self):
           self.client=Client()
           response = self.client.get('/finalap/sahiyta')
           self.assertEqual(response.status_code, 404)
class urltestcase3(TestCase):
    def setUp(self):
        #self.createadmin=User.objects.create_user(username="test user",email="test@gmail.com",password="test password")
        self.client=None
        self.request_url='/finalapp/api/'
    def test_api(self):
        self.client=Client()
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
    def test_api_invalid(self):
        self.client=Client()
        response = self.client.get('/randomurl/')
        self.assertEqual(response.status_code, 404)




class DocumentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@gmail.com", password="Hello World")
        def create_Model(self, name="apple", category="Abstract", image="apple.png",uploaded_at="28-05-2018",rating="5",total_image_downloads="500",countlikes="500"):
         user = Document(user=User)
         return Document.objects.create(name=name, category=category, image=image,uploaded_at=uploaded_at,rating=rating,total_image_downloads=total_image_downloads,countlikes=countlikes)

    def test_model_creation(self):
        self.assertTrue((self.user, 'image_set'))
class ModelFormTest(TestCase):
    def test_valid_form_data(self):
        image_io = BytesIO() # BytesIO has to be used, StrinIO isn't working
        image = Image.new(mode='RGB', size=(200, 200))
        image.save(image_io, 'JPEG')
        form_data = {
                'name': "apple",'category':"Food"
            }
        image_data = {
            'image': InMemoryUploadedFile(image_io, None, 'randomimage.jpg', 'apple/jpeg', len(image_io.getvalue()), None)
        }
        form = DocumentForm(data=form_data, files=image_data)
        self.assertTrue(form.is_valid())
