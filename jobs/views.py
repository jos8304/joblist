from django.shortcuts import render

# Create your views here.

def jobs(request):
    return render(request, 'jobs/index.html')