
from django.db import router
from django.urls import path, include

from apiapp.views import article_list, article_detail,ArticleViewset,GenericAPIdetails,GenericAPIView, ArticleDetails,ArticleAPIView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewset, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    
    
    #function based
    #path('article/', article_list),
    #path('detail/<int:pk>/', article_detail),
    
    #class based
    #path('article/', ArticleAPIView.as_view()),
    #path('detail/<int:id>/', ArticleDetails.as_view()),
    
    #Generic
    path('generic/article/', GenericAPIView.as_view()),
    path('generic/detail/<int:id>/', GenericAPIdetails.as_view()),
]
