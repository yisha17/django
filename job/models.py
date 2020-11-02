from django.db import models
from employer.models import Employer
from django.utils import timezone
from datetime import timedelta

class JobCatagories(models.Model):
    job_catagories = models.CharField(max_length = 60)

    def __str__(self):
        return self.job_catagories

class JobDescription(models.Model):
    EXPERIENCE = [
        ('senior','senior'),
        ('junior','junior'),
        ('manager','manager')
    ]
    TYPE = [
        ('full time','full time'),
        ('contract','contract'),
        ('part time','part time'),
        ('freelancer','freelancer'),
        ('internship','internship')
    ]
    company_name = models.ForeignKey(Employer,on_delete=models.CASCADE)
    job_position = models.CharField(max_length = 50)
    job_type = models.CharField(max_length =10,choices = TYPE)
    address = models.CharField(max_length = 100)
    location = models.CharField(max_length= 30,default = 'Addis Ababa')
    post_date = models.DateTimeField(auto_now=True)
    deadline = models.DateField(help_text="help")
    experience_level = models.CharField(max_length = 10,choices = EXPERIENCE)
    JobCatagories = models.ForeignKey(JobCatagories,on_delete= models.CASCADE)
    Job_description = models.TextField()
   
    

    def __str__(self):
        return self.job_position

    


