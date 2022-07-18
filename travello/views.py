
from django.shortcuts import render

from . models import Destination

# Create your views here.
def index(request):
    # render = 'combination of static content and dynamic content'
    dests = Destination.objects.all()
    
    
    
    
    
    return render(request,'index.html',{'dests':dests}) 
# whenever the client request for home then we need to give the result in response format thats y we use HttpResponse.
