from django.shortcuts import render

job = [
    
   

    {
        'company': 'Tikur Anbessa hospital',
        'job': 'Nurse',
        'job_type':'Full Time',
        'experience':'senior',
        'location':'Addis Ababa',
        'address':'4 kilo next to Ambassador stationary',
        'date_posted': 'semptember 24, 2020',
        'date_ended':'october 6, 2020',
    } ,

    {
        'company': 'Commercial Bank Of Ethiopia',
        'job': 'Custom Service Officer',
        'job_type':'Full Time',
        'experience':'senior',
        'location':'Addis Ababa',
        'address':'4 kilo next to Ambassador stationary',
        'date_posted': 'semptember 12, 2020',
        'date_ended':'october 8, 2020',
    } ,
    {
        'company': 'Commercial Bank Of Ethiopia',
        'job': 'Custom Service Officer',
        'job_type':'Full Time',
        'experience':'senior',
        'location':'Addis Ababa',
        'address':'4 kilo next to Ambassador stationary',
        'date_posted': 'semptember 12, 2020',
        'date_ended':'october 8, 2020',
    }

]


def home(request):
    context = {'job': job} 
    return render(request,'job/index.html',context)
