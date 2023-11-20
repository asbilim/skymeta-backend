from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ArticleViewset, CommentViewSet, LikeViewSet






router = SimpleRouter()
router.register(r'articles', ArticleViewset)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

