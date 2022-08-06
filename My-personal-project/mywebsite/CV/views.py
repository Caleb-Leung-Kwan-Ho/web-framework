from django.shortcuts import render
from .models import CCVV

# Create your views here.
def cv(request):
    exps=CCVV.objects.all().order_by('start_date').reverse()
    return render (request, 'CV/cv.html',{'exps':exps})