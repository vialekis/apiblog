from rest_framework import generics
from posts.models import Post, Category
from posts.api.serializers import PostSerializer, CategoriesSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryPostDetailView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self,**kwargs):
        return Post.objects.filter(status="published").filter(category__slug = self.kwargs['category'])


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer