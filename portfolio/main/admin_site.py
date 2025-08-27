from django.contrib.admin import AdminSite
from .models import Profile,project,Skill,about
from .admin import AdminSkill,AdminAbout,AdminProject,AdminProfile
#In order to make custom admin dashboard

class PortfolioAdminSite(AdminSite):
    site_header = "Portfolio Dashboard"
    site_title = "Portfolio Admin"
    index_title = "Welcome to Portfolio Dashboard"
    index_template = "admin/custom_index.html"

# object created for portfolio admin site (custom site)
portfolio_admin_site = PortfolioAdminSite(name="portfolio_admin")

#registering model
portfolio_admin_site.register(Profile,AdminProfile)
portfolio_admin_site.register(about,AdminAbout)
portfolio_admin_site.register(project,AdminProject)
portfolio_admin_site.register(Skill,AdminSkill)