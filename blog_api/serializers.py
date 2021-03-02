from rest_framework import serializers
from blog.models import Post

# serializer converts data from database into readable form by python
class PostSerializer(serializers.ModelSerializer): 
    # define model and what data in model we want to manage
    class Meta: 
        model = Post 
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
