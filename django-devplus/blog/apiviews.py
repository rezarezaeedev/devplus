from urllib import response
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models                 import Post
from .serializers            import PostSerializer
from rest_framework import status


class PostViews(ViewSet):
    def list(self, request):
        queryset    = Post.objects.filter(is_active=1)
        serializer  = PostSerializer(queryset, many=1, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
