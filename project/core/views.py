from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .forms import CustomAuthenticationForm

def home(request):
    return render(request, "core/index.html")

class CustomLoginView():
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"
    