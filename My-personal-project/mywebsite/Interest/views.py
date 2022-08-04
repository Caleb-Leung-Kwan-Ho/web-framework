from django.shortcuts import render

# Create your views here.
def interest_list(request):
    return render( request,'Interest/interest_list.html' )