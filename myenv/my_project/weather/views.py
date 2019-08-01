
#Views in Django are either functions or classes. 
#In our case since we're creating a simple view, we'll create a function.
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'weather/index.html')
    #render()