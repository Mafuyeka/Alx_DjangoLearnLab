# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    path('posts/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    path('search/', views.SearchResultsView.as_view(), name='search'),
    path('tags/<str:tag_name>/', views.TagPostListView.as_view(), name='posts_by_tag'),
]
