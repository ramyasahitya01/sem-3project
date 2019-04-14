from rest_framework import serializers
from finalapp.models import Document
from django.contrib.auth.models import User
from PIL import Image
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password',)
class DocumentSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    image = serializers.ImageField(
        max_length=None, use_url=True
    )
    class Meta:
          model=Document
          fields=('name','category','image','user')
          def create(self,validated_data):
              user_data=validated_data.pop('user')
              user=user.objects.create(**user_data)
              name=validated_data['name']
              category=validated_data['category']
              image=validated_data['image']
              documents=Document.objects.create(user=user,**validated_data)
              return documents
