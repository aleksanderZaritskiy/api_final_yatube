from rest_framework import routers

from django.urls import include, path

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


VERSION_API = 'v1'

router_v1 = routers.SimpleRouter()

router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path(f'{VERSION_API}/', include(router_v1.urls)),
    path(f'{VERSION_API}/', include('djoser.urls.jwt')),
]
