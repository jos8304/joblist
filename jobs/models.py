from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(max_length=5000)
    # Choices for job type
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
         ('Part Time', 'Part Time'),
         ('Internship', 'Internship'),
         ('Contract', 'Contract'),
    ]   
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)

    # Choices for experience level
    EXPERIENCE_LEVEL_CHOICES = [
        ('Entry Level', 'Entry Level'),
         ('Mid Level', 'Mid Level'),
         ('Senior Level', 'Senior Level'),
         ('Executive', 'Executive'),
    ]
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES)

    # Choices for category
    CATEGORY_CHOICES = [
        ('IT', 'IT'),
         ('Finance', 'Finance'),
         ('Marketing', 'Marketing'),
         ('Human Resources', 'Human Resources'),
         ('Engineering', 'Engineering'),
         ('Education', 'Education'),
         ('Healthcare', 'Healthcare'),
         ('Retail', 'Retail'),
         ('Customer Service', 'Customer Service'),
         ('Sales', 'Sales'),
         ('Project Management', 'Project Management'),
         ('Design', 'Design'),
         ('Construction', 'Construction'),
         ('Manufacturing', 'Manufacturing'),
         ('Research', 'Research'),
         ('Legal', 'Legal'),
         ('Public Relations', 'Public Relations'),
         ('Food Service', 'Food Service'),
         ('Travel', 'Travel'),
         ('Real Estate', 'Real Estate'),
         ('Media', 'Media'),
         ('Art', 'Art'),
         ('Music', 'Music'),
         ('Fitness', 'Fitness'),
         ('Sports', 'Sports'),
         ('Government', 'Government'),
         ('Non-Profit', 'Non-Profit'),
         ('Other', 'Other'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)   

    # Choices for education level
    EDUCATION_LEVEL_CHOICES = [
        ('High School Diploma', 'High School Diploma'),
         ('Associate Degree', 'Associate Degree'),
         ('Bachelor\'s Degree', 'Bachelor\'s Degree'),
         ('Master\'s Degree', 'Master\'s Degree'),
         ('Doctorate Degree', 'Doctorate Degree'),
         ('Professional Certification', 'Professional Certification'),
         ('Vocational Training', 'Vocational Training'),
         ('On-the-job Training', 'On-the-job Training'),
         ('No Degree Required', 'No Degree Required'),
         ('Other', 'Other'),
    ]
    education_level = MultiSelectField(max_length=50, choices=EDUCATION_LEVEL_CHOICES)      


    # Choices for industry
    INDUSTRY_CHOICES = [
        ('Technology', 'Technology'),
         ('Finance', 'Finance'),
         ('Healthcare', 'Healthcare'),
         ('Education', 'Education'),
         ('Retail', 'Retail'),
         ('Manufacturing', 'Manufacturing'),
         ('Hospitality', 'Hospitality'),
         ('Construction', 'Construction'),
         ('Media', 'Media'),
         ('Government', 'Government'),
         ('Non-Profit', 'Non-Profit'),
         ('Other', 'Other'),
    ]
    industry = MultiSelectField(max_length=50, choices=INDUSTRY_CHOICES)
    location = models.CharField(max_length=100)

    # Choices for remote work
    REMOTE_WORK_CHOICES = [
        ('Remote', 'Remote'),
         ('Hybrid', 'Hybrid'),
         ('On-site', 'On-site'),
    ]
    remote_work = MultiSelectField(max_length=20, choices=REMOTE_WORK_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    # Job Features
    # Choices for job features
    JOB_FEATURES_CHOICES = [
        ('Flexible Schedule', 'Flexible Schedule'),
        ('Competitive Salary', 'Competitive Salary'),
        ('Medical Insurance', 'Medical Insurance'),
        ('Dental Insurance', 'Dental Insurance'),
        ('Vision Insurance', 'Vision Insurance'),
        ('401(k) Retirement Plan', '401(k) Retirement Plan'),
        ('Paid Time Off', 'Paid Time Off'),
        ('Paid Sick Leave', 'Paid Sick Leave'),
        ('Tuition Reimbursement', 'Tuition Reimbursement'),
        ('Professional Development', 'Professional Development'),
        ('Relocation Assistance', 'Relocation Assistance'),
        ('Employee Discounts', 'Employee Discounts'),
        ('Company Events', 'Company Events'),
        ('Work-Life Balance', 'Work-Life Balance'),
        ('Career Growth Opportunities', 'Career Growth Opportunities'),
        ('Mentoring Program', 'Mentoring Program'),
        ('Employee Recognition Program', 'Employee Recognition Program'),
        ('Employee Assistance Program', 'Employee Assistance Program'),
        ('Other', 'Other'),
    ]
    job_features = MultiSelectField(choices=JOB_FEATURES_CHOICES, max_length=200)
    

    def __str__(self):
        return self.title