from django.shortcuts import render
from .models import soft_skills

# Create your views here.
def Soft_skills(request):
    skills= soft_skills.objects.all().order_by('level').reverse()
    return render (request, 'softskills/softskills.html',{"soft_skills":skills})