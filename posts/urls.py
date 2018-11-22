from django.conf.urls import url, include

from posts.views import PostListView, CommentListView


urlpatterns = [
    url(r"^posts/", PostListView.as_view()),
    url(r"^comments/", CommentListView.as_view())
]
