from django.shortcuts import render
from .models import CV

# Create your views here.
def cv(request):
    exps=CV.objects.all().order_by('start_date')
    return render (request, 'CV/cv.html',{'exps':exps})