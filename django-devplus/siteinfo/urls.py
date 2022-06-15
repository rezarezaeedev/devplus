from rest_framework.routers  import SimpleRouter
from .apiviews import SiteInfoViews

router = SimpleRouter()
router.register(r'siteinfo', SiteInfoViews, basename='siteinfo')

urlpatterns = [
     
] + router.urls
