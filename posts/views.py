from rest_framework import status
from rest_framework.views import APIView

from posts.models import Post, Comment
from utils.common import create_response
from posts.serializers import PostSerializer, CommentSerializer


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return create_response(data=serializer.data, status=status.HTTP_200_OK)


class CommentListView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return create_response(data=serializer.data, status=status.HTTP_200_OK)
