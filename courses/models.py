# courses/models.py
from django.db import models

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('agriculture', 'Agriculture'),
        ('finance', 'Finance'),
        ('tech', 'Tech'),
        ('other', 'Other'),
        ('food', 'Food'),
    ]

    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=255)
    youtube_video_id = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    producer = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, blank=True,null=True)

    def __str__(self):
        return self.title




from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = '__all__'
