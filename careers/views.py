from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from careers.models import CareerPost
from careers.serializer import PostSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
  queryset = CareerPost.objects.all()
  serializer_class = PostSerializer