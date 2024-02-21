from django.db import models

# Create your models here.

class CareerPost(models.Model):
  id = models.AutoField(primary_key=True, editable=False);
  username = models.CharField(max_length=100);
  created_datetime = models.DateTimeField(auto_now_add=True, editable=False);
  title = models.CharField(max_length=255);
  content = models.TextField();
