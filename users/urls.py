from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from users import views

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('login/', views.UserAPI.as_view(), name='user_api'),
    path('update/<int:user_id>', views.UserView.as_view(), name='user_update'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
