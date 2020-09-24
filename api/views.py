from rest_framework import permissions, viewsets
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from posts.models import Post, Comment
from api.serializers import PostSerializer, CommentSerializer
from api.permissions import IsAuthorOrReadOnlyPermission


class APIPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnlyPermission]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


    def perform_destroy(self, serializer):
        serializer.delete()


class APICommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnlyPermission]

    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def list(self, request, post_pk):
        comments = Comment.objects.filter(post=post_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
