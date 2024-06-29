from django.shortcuts import render

# Create your views here.
# FBV "home"
def home(request):
    return render(request, "sales/home.html")
