from dataclasses import field
from rest_framework import serializers
from .models import PostApi

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostApi
        fields = ['id', 'title', 'desc', 'slug']