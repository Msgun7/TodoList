from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# JWT 공식 자료에서 simple JWT를 사용하기 위해 추가해줘야하는 부분

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('edit/', views.UserView.as_view(), name='eidt'),
    path('signout/', views.UserView.as_view(), name='signout'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:id>/', views.UserView.as_view(), name='user_view'),
]
# app을 추가할 시 메인 앱의 url에 이어주기위한 include와 path를 추가
