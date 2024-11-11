from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.views import View
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def register(request):
    if request.method == 'GET':
        print('we are in the get method')

        context={
        'page_name' : 'Register'
    }
        return render(request, 'accounts/register.html', context)

    elif request.method == 'POST':  
        print('we are in the post method')  
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = User.objects.create_superuser(username=username,password=password)
        return redirect('/')

class Register(View):
    def get(self,request):
        print('get method')

        context={
        'user_form' : UserRegisterform(),
        'customer_form' : CustomerRegisterForm(),
        'page_name' : 'Register',
         }
        return render(request, 'accounts/register.html', context)
    

    def post(self,request):  
      #  print('post method')  
      #  username = request.POST.get('Username')
      #  password = request.POST.get('password')
      #  user = User.objects.create_superuser(username=username,password=password)
       # print(user)
       user_form = UserRegisterform(data=request.POST)
       customer_form = CustomerRegisterForm(data=request.POST,files=request.FILES)
       context={
               'page_name' : 'Register',
               'user_form' : user_form,
               'customer_form' : customer_form,
               
           }
       if user_form.is_valid() and customer_form.is_valid():
         user = user_form.save(commit=False)
         password=request.POST.get('password')
         confirm_password = request.POST.get('confirm_password')
         if password == confirm_password:
             user.password=password
         else:
             messages.error(request,'Password and confirm password are not same')
             messages.error(request,'make sure Password and confirm password are same')


             return render(request,'accounts/register.html',context)    

         user.save()
         customer = customer_form.save(commit=False)
         customer.dob = request.POST.get('dob')
         customer.user = user
         customer.save()
         return redirect('login')

       else:
           messages.error(request,'fill in the form correctly')
           return render(request,'accounts/register.html/',context)
       
       return redirect('/')
           

class Login(View):
    def get(self,request):
        return render(request, 'accounts/login.html')
    


    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'login successfull')
            messages.info(request,f'Welcome user {user.username}')
            return redirect('/')
        else:
            messages.error(request,'authentication failed')
            return redirect('login')









def logout_user(request):
    logout(request)
    return redirect('/')