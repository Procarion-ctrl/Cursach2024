from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from authentication.views import RegistrationApiView, LoginApiView, LogoutView

urlpatterns = [
    path('register/', RegistrationApiView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


