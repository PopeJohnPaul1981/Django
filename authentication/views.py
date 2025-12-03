from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def loginpage(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("homepage")
    else: 
        form = AuthenticationForm()
    return render(request,"login.html",{"form":form})

def registerpage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("homepage")
    else: 
        form = UserCreationForm()
    return render(request,"register.html",{"form":form})


def userlogout(request):
    if request.method == "POST":
        logout(request)
        return redirect("loginpage")