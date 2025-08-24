from rest_framework import serializers
from .models import Post, Comment, Like
from notifications.models import Notification  # Correct import

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='like_set.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'created_at', 'likes_count']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
