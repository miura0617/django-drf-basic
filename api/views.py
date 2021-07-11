from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .ownpermissions import ProfilePermission

# Create your views here.

# ModelViewSetは、CRUDがすべて使えるようになっている
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # AllowAnyでだれでもアクセスし、読み込んだり、書き込んだりできるようにする
    # permission_classes = (AllowAny,)
    permission_classes = (ProfilePermission,)

# /myselfのためのView：ログインしたユーザの情報取得、または更新するだけ
class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    # /myselfは、ログインしているユーザだけが見れる情報なので、TokenAuthenticationで認証通った人だけ見れるようにする
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # getで返ってくるオブジェクトは、ログインしているユーザ情報だけを返す
    def get_object(self):
        return self.request.user


# ModelViewSetは、CRUDがすべて使えるようになっている
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # /tasksもログインしているユーザだけが見れる情報なので、TokenAuthenticationで認証通った人だけ見れるようにする
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

