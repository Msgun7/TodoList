from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('ToDo/', include("ToDo.urls")),
]


# app을 추가할 시 메인 앱의 url에 이어주기위한 include아 path를 추가
