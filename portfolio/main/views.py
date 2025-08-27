from django.shortcuts import render,redirect
from . import views
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Profile,about,Skill,project
# Create your views here.
def homepage(request):
    profiles = Profile.objects.all()
    return render(request ,"home.html",{"profiles" : profiles})
def aboutpage(request):
    profiles = Profile.objects.all()
    abouts = about.objects.all()
    skills = Skill.objects.all()
    return render(request,"about.html",{"abouts" : abouts, "skills" : skills ,"profiles" : profiles})
def contactview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            #sending email to me:
            send_mail(
                subject=f"New Contact message from {form.cleaned_data['name']}",
                message= form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list= ['muhammadalirana40702@gmail.com'],
                )
            #---------------------------------------------------------------
            messages.success(request,'your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request,'Please correct the errors below.')
    else:
         form = ContactForm()           
    return render(request,"contact.html", {'form' : form})
def projectpage(request):
    projects = project.objects.all()
    return render(request,"projects.html",{"projects" : projects})