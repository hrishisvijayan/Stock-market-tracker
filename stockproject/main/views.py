
from django.shortcuts import render

# Create your views here.

def home(self):
    return render(self,'main/basic.html')
