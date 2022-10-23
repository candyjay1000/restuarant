from django.shortcuts import  render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.contrib import messages
# Create your views here.
def contact(request):
    form=ContactForm(request.POST or None)
    context={
        'title':'SIGN UP',
        'form':form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,'message sent successfully')
            return redirect(reverse('blogs'))
        else:
            print(form.errors)
            messages.error(request,'unsuccessful')	
    return render(request,'contact/contact.html',context)
