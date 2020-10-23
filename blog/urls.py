from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('create_post/',views.create_post, name='create_post'),
    path('display_posts/',views.display_posts,name='display_posts'),
    path('display_posts/<int:id>/',views.display_post,name='display_post'),
    path('delete_post/<int:id>/',views.delete_post,name='delete_post'),
    path('edit_post/<int:id>/',views.edit_post,name='edit_post'),
    path('add_comment/<int:post_id>/',views.add_comment,name='add_comment'),
    path('delete_comment/<int:post_id>/<int:comment_id>/',views.delete_comment, name='delete_comment'),
    path('edit_comment/<int:post_id>/<int:comment_id>/',views.edit_comment, name='edit_comment'),
    path('like_post/<int:post_id>/',views.like_post, name='like_post'),
    path('dislike_post/<int:post_id>/',views.dislike_post, name='dislike_post'),
    path('display_my_posts/',views.display_my_posts, name='display_my_posts')

]