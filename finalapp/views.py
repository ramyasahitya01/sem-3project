from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib.auth.models import User
from .models import  Document
from rest_framework.decorators import api_view
from rest_framework.response import Response
from finalapp.serializers import DocumentSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
import os
from .forms import DocumentForm
def home(request):
    return render(request, 'finalapp/home.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            formInstance = form.save(commit=False)
            formInstance.user = request.user

            formInstance.save()
            return redirect('../../homepage/profile_view')
    else:
        form = DocumentForm()
    return render(request, 'finalapp/model_form_upload.html', {
        'form': form
    })
def searchdata(request):
     if request.method=="GET":
         key=request.GET.get('searchword')

         searchedlist=Document.objects.filter(Q(category__icontains=key) | Q(name__icontains = key))
         items=[]
         context={'items':searchedlist}
         print(context)
     return render(request,'myapp/category/index.html',context)
class DocumentListView(APIView):
    def get(self,request):
        documents=Document.objects.all()
        serializer=DocumentSerializer(documents,many=True)
        return Response(serializer.data)
