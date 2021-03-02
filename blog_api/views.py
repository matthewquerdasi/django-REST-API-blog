from rest_framework import generics
from blog.models import Post 
from .serializers import PostSerializer

# Post list view: list and create items 
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all() # retreives all 'published' posts 
    serializer_class = PostSerializer # points to serializers.py 

# Post detail view: get and delete items
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

