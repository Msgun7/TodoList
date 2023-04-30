from django.urls import path
from ToDo import views

# JWT 공식 자료에서 simple JWT를 사용하기 위해 추가해줘야하는 부분

urlpatterns = [
    path('', views.TodosView.as_view(), name='todos_view'),
    path('<int:id>/', views.TodoDetailView.as_view(), name='todo_detail_view'),
]
# app을 추가할 시 메인 앱의 url에 이어주기위한 include와 path를 추가
