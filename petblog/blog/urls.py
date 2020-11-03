from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('like/',views.like,name='like_post'),
    path('add-comment/',views.add_comment,name='add_comment'),

]