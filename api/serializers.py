from rest_framework import serializers
from blogapp.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    class Meta:
        model = Post
        fields = ['id','title','description','created_at','author']
        read_only_fields = ['id','created_at','author']
        

