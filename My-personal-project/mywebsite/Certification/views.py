from django.shortcuts import render
from .models import certif_list

# Create your views here.
def certified_list(request):
    archivements= certif_list.objects.all().order_by('rank')
    return render (request, 'Certification/certif_list.html',{'certifs':archivements})