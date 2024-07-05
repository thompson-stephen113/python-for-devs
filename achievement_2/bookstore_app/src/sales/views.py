from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# FBV "home"
def home(request):
    return render(request, "sales/home.html")

# FBV "records", protected
@login_required
def records(request):
    return render(request, "sales/records.html")
