from django.urls import path, re_path
from . import views
app_name='finalapp'
urlpatterns = [
    path('',views.home,name="home"),
    path('upload/',views.model_form_upload,name='model_form_upload'),
    path('searchdata/',views.searchdata,name='searchdata'),
    path('api/',views.DocumentListView.as_view())
]
