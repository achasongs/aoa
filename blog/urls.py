from django.urls import path
# from .import views
from .views import BlogHome, ArticleDetailView, AddPostView, UpdatePostView

urlpatterns = [
    path('', BlogHome.as_view(), name="blog"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'), 
]
