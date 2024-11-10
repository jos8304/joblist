from django.shortcuts import render
from .models import Job

# Create your views here.

def jobs(request):
    jobs = Job.objects.all()
    job_location = Job.objects.values_list('location', flat=True).distinct()
    job_category = Job.objects.values_list('category', flat=True).distinct()

    context = {
        'jobs': jobs,
        'job_location' : job_location,
        'job_category' : job_category,
    }
    
    return render(request, 'jobs/jobs.html',context)
