from rest_framework.routers  import SimpleRouter
from .apiviews import PostViews

router = SimpleRouter()
router.register(r'posts', PostViews, basename='posts')

urlpatterns = [
     
] + router.urls
