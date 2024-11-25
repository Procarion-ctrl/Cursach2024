from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Investment
from .serializers import InvestmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class InvestmentView(APIView):
    permission_classes = [IsAuthenticated]  # Вимагає аутентифікації для цього ендпоінта
    
    def post(self, request):
        data = request.data.copy()  # Копіюємо дані, щоб мати можливість модифікувати їх
        data['user'] = request.user.id  # Додаємо ID користувача до даних
        
        serializer = InvestmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # Зберігаємо інвестицію з прив'язаним користувачем
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PortfolioView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Використовуємо існуючий токен, а не генеруємо новий
        if request.user.is_authenticated:
            investments = Investment.objects.filter(user=request.user)
            serializer = InvestmentSerializer(investments, many=True)
            return Response(serializer.data)
        return Response({'detail': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
