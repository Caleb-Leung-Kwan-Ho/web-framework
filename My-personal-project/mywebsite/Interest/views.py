from django.shortcuts import render
from .models import Interest

# Create your views here.
def interest_list(request):
    hobbies=Interest.objects.all().order_by('rank')
    return render( request,'Interest/interest_list.html',{'Interest':hobbies} )