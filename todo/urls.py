from django.urls import path
from todo import views

urlpatterns = [
    path('', views.todo_view.as_view(), name='index'),
    path('', views.todo_view.as_view(), name='add'),
    path('<int:pk>/', views.todo_view.as_view(), name='edit'),
    path('<int:pk>/delete/', views.todo_view.as_view(), name='delete')
]
