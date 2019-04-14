from django.shortcuts import render
from homepage.forms import UserForm,FeedbackForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django import forms
from django.contrib import messages
from homepage.models import feedback
from django.shortcuts import redirect
from finalapp.models import Document
from homepage.models import UserProfileInfo
def index(request):
    my_list=Document.objects.order_by('-pk')

    my_dict={'new_images':my_list}

    return render(request,'homepage/index.html',my_dict)



def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        re_password=request.POST.get('re_password')
        password=request.POST.get('password')
        print(password,"\n",re_password)
        if re_password==password:
            if user_form.is_valid():
                user=user_form.save()
                user.set_password(user.password) #hashing the password
                user.save() #save hash password to database
                registered=True
            else:
                print("something is fishy")
        else:

            raise forms.ValidationError("Passwords do not match.Please Re_enter them")

            raise forms.ValidationError("Passwords do not match")

    else:
        user_form=UserForm()

    return render(request,'homepage/registration.html',{'user_form':user_form,'registered':registered,})

@login_required
def special(request):
    return HttpResponse("You are logged in dude")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to login and failed")
            print("username:{} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'homepage/login.html')
def user_feedback(request):
    if request.method=="POST":
        feedback_form=FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            feedback=feedback_form.save()
            feedback.save()
            print(feedback_form.cleaned_data['text'])
        return HttpResponseRedirect(reverse('index'))
    return render(request,'homepage/feedback.html')
def display_feedback(request):
    feedbacks=feedback.objects.order_by('-pk')

    sum=0
    count=0
    for i in feedbacks:
        sum=sum+int(i.rating)
        count=count+1
    avg_rating=sum/count
    print(sum)
    print(avg_rating)
    my_dict={'feedbacks':feedbacks,'avg_rating':avg_rating}
    return render(request,'homepage/display_feedbacks.html',my_dict)

def profile_view(request):

    info_object,created = UserProfileInfo.objects.get_or_create(user=request.user)
    user_name=request.user.username
    print(user_name)
    images=Document.objects.filter(user=request.user)
    my_dict = {'user': user_name, 'images': images, 'bio': info_object.bio, 'phone': info_object.phone,'city': info_object.city}
    return render(request,'homepage/user_profile.html', my_dict)
def delete_image(request,value):
    Document.objects.filter(name=value).delete()

    info_object,created = UserProfileInfo.objects.get_or_create(user=request.user)
    user_name=request.user.username
    print(user_name)
    images=Document.objects.filter(user=request.user)
    my_dict = {'user': user_name, 'images': images, 'bio': info_object.bio, 'phone': info_object.phone,'city': info_object.city}
    return render(request,'homepage/user_profile.html', my_dict)
def edit_profile(request):
    if request.method=="POST":
        bio=request.POST.get('bio')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        user=request.user
        info_object,created=UserProfileInfo.objects.get_or_create(user=user)
        info_object.bio=bio
        info_object.phone=phone
        info_object.city=city
        info_object.save()

        user_name = request.user.username
        print(user_name)
        images = Document.objects.filter(user=request.user)
        my_dict = {'user': user_name, 'images': images,'bio':info_object.bio,'phone':info_object.phone,'city':info_object.city}
        return render(request, 'homepage/user_profile.html', my_dict)
    return render(request,'homepage/edit_profile.html')

def update_image(request,value):
    if request.method=="POST":
        name=request.POST.get('name')
        category=request.POST.get('category')
        image_info_object=Document.objects.get(name=value)
        image_info_object.name=name
        image_info_object.category=category
        image_info_object.save()
        return redirect(reverse('homepage:profile_view'))

    return render(request,'homepage/update_image.html',{'name':value})



