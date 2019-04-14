
from django.urls import path
from myapp import views


app_name='myapp'

urlpatterns=[
     path('index/(?P<value>\s+)',views.index,name='index'),
    path('category',views.category,name='category'),
    path('likes/(?P<imageid>\s+)',views.countlikes,name='countlikes'),
     path('user/(?P<value>\s+)',views.user,name='user'),
    path('logout/', views.user_logout, name='logout'),

]
