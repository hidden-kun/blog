from django.urls import path
from post import views


urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/category/<slug:slug>/', views.PostByCategory.as_view(), name='posts_by_category')
]