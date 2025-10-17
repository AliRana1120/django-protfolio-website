from django.db import models

# Create your models here.
class ContactMsg(models.Model):
    name = models.CharField(max_length=100)
    email =  models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return f'Message from {self.name}'
    
#ADMIN ONLY
class Profile(models.Model):
    myname = models.CharField(max_length=50)
    myskill = models.CharField(max_length=50)
    portfolioDesc = models.CharField(max_length=500)
    cvlink = models.URLField(max_length=500)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=500)
    myemail = models.EmailField(max_length=254)
    picture = models.ImageField(upload_to="profile_pics/", height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
       return self.myname
    

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        

class about(models.Model):
    myname = models.ForeignKey("main.profile", verbose_name=("Full Name"), on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    location = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    STATUS_CHOICES = [
        ("available", "Available"),
        ("not_available", "Not Available"),
    ]
    freelance = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available"
    )
    skills =  models.ManyToManyField(Skill)
    
    def __str__(self):
      return f"{self.myname} {self.education}"
    
 
class project(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    projectlink = models.URLField(max_length=200)
    projectgithub = models.URLField(max_length=200,null=True,blank=True)
    projectimg = models.ImageField(upload_to="profile_pics/",null=True,blank=True, height_field=None, width_field=None, max_length=None)
 
    def __str__(self):
      return self.title