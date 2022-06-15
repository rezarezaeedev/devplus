from urllib import response
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models                 import SiteInfo
from .serializers            import SiteInfoSerializer
from rest_framework import status


class SiteInfoViews(ViewSet):
    def list(self, request):
        queryset    = SiteInfo.objects.filter(is_active=1).last()
        serializer  = SiteInfoSerializer(queryset, many=0, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
