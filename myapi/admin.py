# here we register the different tables we want to show in the admin panel
# i created this, the superuser, the admin page
# all to see the database whilst I was developing the program
from django.contrib import admin
from .models import Provider

# this line of code registers the model on the admin site
admin.site.register(Provider)