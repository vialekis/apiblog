from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from posts.models import Post, Category
from django.http import JsonResponse


class PostsListView(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = "posts"

class PostView(DetailView):
    model = Post
    context_object_name = "post"
    queryset = Post.objects.all()


def CategoryPostsListView(request,**kwargs):
    queryset = Post.objects.filter(status="published").filter(category__slug = kwargs["category"])
    return render(request,"posts/categorypost_list.html", {"posts": queryset, "category": kwargs["category"]},)


class CategoryListView(ListView):
    print("CategoryListView")
    queryset = Category.objects.all()
    context_object_name = "categories"


def json_list_published_posts(request):
    posts = Post.objects.filter(status="published")

    return JsonResponse({
        "posts": [{
                    "title": p.title,
                    "slug": p.slug,
                    "id": p.id,
                    "published": p.when_published,
                    "category":p.category
        }
                for p in posts]
    })