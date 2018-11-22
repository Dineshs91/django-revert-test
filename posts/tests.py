from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from posts.models import Post, Comment


class PostTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        post = Post.objects.create(
            title="post1",
            description="post1 description"
        )

        Comment.objects.create(
            text="Comment for post1",
            post=post
        )

    def test_get_posts(self):
        response = self.client.get("/api/posts/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_comments(self):
        response = self.client.get("/api/comments/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
