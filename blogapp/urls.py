from django.urls import path
from blogapp.views import PostView,AddPost,UpdatePost,DeletePost,PostDetail


urlpatterns = [
    path('',PostView.as_view(),name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('add/',AddPost.as_view(),name='add'),
    path('update/<int:pk>/',UpdatePost.as_view(),name='update'),
    path('delete/<int:pk>/',DeletePost.as_view(),name='delete'),

]
