from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken 
from autentication.serializers import UserSerializer

class RegistrationApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Користувач успішно створений'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
           refresh = RefreshToken.for_user(user)
           access_token = str(refresh.access_token)

           response = Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
           response.set_cookie(
               'access_token', access_token, httponly=True, samesite='None', secure=False
           )
           response.set_cookie(
               'refresh_token', str(refresh), httponly=True, samesite='None', secure=False
           )
           print("Cookies set with access token:", access_token)
           return response
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def get(self):
        response = Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response
