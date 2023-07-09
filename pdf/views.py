from django.shortcuts import render, redirect
from .models import Profile
from django.http import HttpResponse
from django.template import loader 
import pdfkit 
import io

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        phone = request.POST.get("phone", "")
        mail = request.POST.get("mail", "")
        education = request.POST.get("education", "")
        skills = request.POST.get("skills", "")
        about = request.POST.get("about", "")
        interests = request.POST.get("interests", "")

        profile = Profile(name=name, phone=phone, mail=mail, education=education, skills=skills, about=about, interests=interests)
        profile.save()
        
    return render(request, "accept.html")

def cv(request, id):
    user = Profile.objects.get(pk=id)
    template = loader.get_template("cv.html")
    html = template.render({'user':user})
    option={
            'page-size': 'Letter',
            'encoding': 'UTF-8',
        }
    pdf = pdfkit.from_string(html, False, option)
    response = HttpResponse(pdf, content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachments'
    filename = "resume.pdf"
    return response

def list(request):
    profile=Profile.objects.all()
    return render(request, "list.html",{'profile':profile})
