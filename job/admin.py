from django.contrib import admin
from .models import JobDescription,JobCatagories

# Register your models here.
admin.site.register(JobDescription)
admin.site.register(JobCatagories)