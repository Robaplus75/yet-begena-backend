# courses/views.py
from rest_framework import generics
from .models import Course, CourseSerializer

# List and Create
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Retrieve, Update, Delete (for a specific course)
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'id'  # We'll use ID in the URL
