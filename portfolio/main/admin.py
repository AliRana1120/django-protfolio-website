from django.contrib import admin
from .models import Profile, project, Skill, about # to import models inside admin panel

class AdminProfile(admin.ModelAdmin):
    #to display my name on dashboard
    list_display = ("myname",)

class AdminAbout(admin.ModelAdmin):
    list_display = ("myname",)

class AdminProject(admin.ModelAdmin):
    list_display = ("title", "projectlink")
    search_fields = ("title",)

class AdminSkill(admin.ModelAdmin):
    list_display = ("name",)
       