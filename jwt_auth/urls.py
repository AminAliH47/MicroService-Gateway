from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from jwt_auth import views

app_name = "jwt_auth"

urlpatterns = (
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginView.as_view(), name="login")
)
