from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import APIPostViewSet, APICommentViewSet


router = DefaultRouter()
router.register('posts', APIPostViewSet)
router.register(r'posts/(?P<post_pk>\d+)/comments', APICommentViewSet, basename='comments')

# comment_method_lc = {
#     'get': 'list',
#     'post': 'create'
# }

# comment_method_rpd = {
#     'get': 'retrieve',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# }

urlpatterns = [
    path('', include(router.urls)),
    # path('posts/<int:post_id>/comments/', APICommentViewSet.as_view(comment_method_lc)),
    # path('posts/<int:post_id>/comments/<int:pk>/', APICommentViewSet.as_view(comment_method_rpd)),
    path('api-token-auth/', views.obtain_auth_token),
]
