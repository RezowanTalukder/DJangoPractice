from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer



class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

    




# Create your views here.


