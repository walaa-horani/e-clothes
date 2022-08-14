from django.shortcuts import render,redirect
from .models import *
from django.http import  HttpResponseRedirect
from .form import SignUpForm
from django.views.generic import CreateView
from django.views import generic
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
        else:
            messages.error(request,'password or username are not correct')
            return redirect('login_user')
    else:        
          return render(request,'store/login.html',)
def logout_user(request):
    logout(request)
    messages.success(request,'logged out successfully')
    return redirect('store')

    

class RegisterForm(generic.CreateView):
    form_class= SignUpForm
    template_name = 'store/register.html'
    success_url = reverse_lazy('login')

def store(request):
    products = Product.objects.all().order_by('-id')
    category = Category.objects.all()

    return render(request,'store/store.html',{'products':products,'category':category})

def category_products(request,id,slug):
    products = Product.objects.filter(category=id)
    category = Category.objects.all()

    return render(request,'store/category_products.html',{'products':products,'category':category})




def details(request,id):
    product = Product.objects.get(id=id)

    return render(request,'store/details.html',{'product':product})


def categories(request):
    category = Category.objects.all()
    
    
    return render(request,'store/categories.html',{'category':category})


def order_product(request):
    profile = Profile.objects.get(user=request.user)
    shopcart= ShopCart.objects.filter(customer= request.user)

    return render(request,'store/order_product.html',{'shopcart':shopcart,'profile':profile})






def cart(request):
    shopcart= ShopCart.objects.filter(customer= request.user)


    return render(request,'store/cart.html',{'shopcart':shopcart})    



def addtocart(request):
    url = request.META.get('HTTP_REFERER')
   
    current_user= request.user


    checkproduct = ShopCart.objects.filter(product=id)
    if checkproduct:
        control = 1

    else:
        control = 0

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(product=id)   
                data.quantity += form.cleaned_data['quantity'] 
                data.save()

            else:
                data = ShopCart()     
                data.customer = current_user.id
                data.product= id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request,'added to cart')
        return HttpResponseRedirect(url)
                

    else:
        if control ==1:
            data = ShopCart.objects.get(product=id)
            data.quantity +=1 
            data.save()

        else:
            data = ShopCart()
            data.customer = current_user
            data.product_id = id  
            data.quantity = 1
            data.save()  

        messages.success(request,'added to cart')
        return HttpResponseRedirect(url)

def profile(request,id):
    userprofile = Profile.objects.get(id=id)

    return render(request,'store/profile.html',{'userprofile':userprofile})       