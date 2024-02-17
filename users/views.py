from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method== "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()       
            username=form.cleaned_data.get("username")
            try:
                messages.success(request,f"Account is created for {username} Successfully!")
                return redirect("blog-home")
            except:
                messages.error(request,f"Invalid credential!  *Please Try Again*")
            
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

