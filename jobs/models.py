# models.py

from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course

# User = get_user_model()

class Job(models.Model):
    JOB_TYPES = [
        ('full-time', 'Full-Time'),
        ('part-time', 'Part-Time'),
        ('internship', 'Internship'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
    ]

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES, null=True, blank=True)
    salary_range = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    requirements = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='related_jobs')

    # posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')

    def __str__(self):
        return self.title


from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

