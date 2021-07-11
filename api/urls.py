from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, UserViewSet, ManageUserView

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    # ManageUserViewのように継承元が「generic」の場合、通常どおりas_view()が使って、パスとビューをつなげる
    path('myself/', ManageUserView.as_view(), name='myself'),
    # TaskViewSetやUserViewSetのように継承元が「viewsets.ModelViewSet」の場合、routersを使ってパスとビューをつなげる
    path('', include(router.urls)),
]
