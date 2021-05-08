from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.viewsets import ModelViewSet
from app01.models import User
from utile.Myserializers import UserModelSerializer, regists2
from utile.Myutie import test

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def list(self, request, *args, **kwargs):
        test(UserModelSerializer)
        return super().list(request, *args, **kwargs)


