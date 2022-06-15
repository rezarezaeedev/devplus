from rest_framework.serializers  import ModelSerializer
from .models                     import SiteInfo


class SiteInfoSerializer(ModelSerializer):
    class Meta:
        model = SiteInfo
        fields = '__all__'
