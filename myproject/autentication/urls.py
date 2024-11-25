from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from autentication.views import RegistrationApiView, LoginApiView, LogoutView

urlpatterns = [
    path('register/', RegistrationApiView.as_view(), name='register'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


