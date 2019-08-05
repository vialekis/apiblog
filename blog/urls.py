"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import PostsListView,  json_list_published_posts, CategoryListView, CategoryPostsListView, CategoryPostsListView, PostView
from posts.api import views as api_views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostsListView.as_view()),
    path('post/<int:pk>', PostView.as_view(), name="postdetail"),
    path("<category>", CategoryPostsListView, name= "categoryPosts"),
    path('categories/', CategoryListView.as_view(),name= "categories"),
    # path('api/posts/', json_list_published_posts),
    path("api/posts/", api_views.PostListView.as_view(), name="api_post_list"),
    path("api/posts/<pk>", api_views.PostDetailView.as_view(), name="api_post_detail"),
    path("api/categories/", api_views.CategoryListView.as_view(), name="api_category_list"),
    path("api/categories/<category>", api_views.CategoryPostDetailView.as_view(), name="api_categorypost_list"),
]
