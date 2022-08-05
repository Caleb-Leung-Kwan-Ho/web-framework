from django.shortcuts import render
from .models import Technical_skills

# Create your views here.
def technical_skills(request):
    skills= Technical_skills.objects.all().order_by('level').reverse()
    return render( request,'technical_skills/technical_skills.html',{"tech_skills":skills})