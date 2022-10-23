from django.shortcuts import  render, redirect
from django.urls import reverse
from .forms import OrderForm
from django.contrib import messages
# Create your views here.
def order(request):
    form=OrderForm(request.POST or None)
    context={
        'title':'SIGN UP',
        'form':form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'order placed successfully')
            return redirect(reverse('order'))
        else:
            print(form.errors)
            messages.error(request,'unsuccessful')	
    return render(request,'order/order.html',context)