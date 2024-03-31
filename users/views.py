from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import UserRegistrationForm

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()

    return render(request, "registration.html", context={"form": form})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request=request, user=user)
            
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse(status=404)
    

def logout(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER'))