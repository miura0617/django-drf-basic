from django.contrib import admin
from django.urls import path
from django.conf.urls import include
# トップの改装は、/admin、/auth、/apiと決めた
# /authでusernameとpasswordをPOSTするとTokenを返すようにするには「obtain_auth_token」が必要
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', obtain_auth_token),

]
