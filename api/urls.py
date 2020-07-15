from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('api/viewset/', include(router.urls)),
    path('api/viewset/<int:pk>/', include(router.urls)),

    path('api/ncb-article-list/', article_list),
    path('api/ncb-detail/<int:pk>/', article_detail),

    path('api/article-list/', ArticleAPIView.as_view()),
    path('api/detail/<int:id>/', ArticleDetails.as_view()),

    path('api/generic-article-list/', GenericAPIView.as_view()),
    path('api/generic-article-list/<int:id>/', GenericAPIView.as_view()),

]