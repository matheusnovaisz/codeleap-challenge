from rest_framework import serializers
from careers.models import CareerPost

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = CareerPost
    fields = ["id", "username", "created_datetime", "title", "content"]

  def create(self, validated_data):
    return CareerPost.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    instance.title = validated_data.get("title", instance.title)
    instance.content = validated_data.get("content", instance.content)
    instance.save()
    return instance
