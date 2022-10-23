from django.shortcuts import  render, redirect
from django.urls import reverse
from .forms import CustomUserForm
from django.contrib.auth import login,logout
from django.contrib import messages
from .email_backend import EmailBackend

# Create your views here.
def index(request):
    context={
        'title': 'HomePage'
    } 
    return render(request,'candy/index.html',context)

def about(request):
    context={
        'title' :'About'
    }        
    return render(request,'candy/about.html',context)

def contact(request):
    context={
        'title': 'Contact'
    }        
    return render(request,'contact/contact.html',context)

def services(request):
    context={
        'title': 'Services'
    }     
    return render(request,'candy/services.html',context)

def team(request):
    context={
        'title': 'Team'
    }     
    return render(request,'candy/team.html',context)

def pricing(request):
    context={
        'title': 'Pricing'
    }     
    return render(request,'candy/pricing.html',context)

def portfolio(request):
    context={
        'title': 'Portfolio'
    }     
    return render(request,'candy/portfolio.html',context)

def portfolio_details(request):
    context={
        'title': 'Portfolio Details'
    }       
    return render(request,'candy/portfolio-details.html',context)

def testimonials(request):
    context={
        'title': 'Testimonials'
    }       
    return render(request,'candy/testimonials.html',context)

def blog(request):
    context={
        'title': 'Blog'
    }       
    return render(request,'candy/blog.html',context)

def sign_up(request):
    form=CustomUserForm(request.POST or None, request.FILES or None)
    context={
        'title':'SIGN UP',
        'form':form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'registration successful')
            return redirect(reverse('sign_in'))
        else:
            messages.error(request,'unsuccessful')	
    return render(request, 'candy/sign-up.html',context)

def sign_in(request):
    context={
        'title':'SIGN IN'
    }
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=EmailBackend.authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request, 'invalid credentials')
            return redirect(reverse('sign_in'))
    else:
            return render(request,'candy/sign-in.html',context)

def sign_out(request):
    logout(request)
    messages.info(request,'logged out')
    return redirect(reverse('homepage'))

def orders(request):
    if request.user.is_authenticated:        
        return render(request,'candy/orders.html')
    else:
        messages.error(request, 'you have to login ')
        return redirect(reverse('sign_in'))
