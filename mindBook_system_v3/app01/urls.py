from django.urls import path
from rest_framework.routers import DefaultRouter
from app01 import views

urlpatterns = []
router = DefaultRouter()
router.register('user', views.UserModelViewSet)


urlpatterns += router.urls
