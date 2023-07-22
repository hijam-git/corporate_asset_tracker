from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from .models import *
from rest_framework.permissions import  AllowAny
from rest_framework.decorators import permission_classes



# View to create a company (registration for the company owner)
@permission_classes([AllowAny])
class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



#---------------View for Staff-------------------

# View to create a staff (registration for a staff member)
@permission_classes([AllowAny])
class StaffCreateView(generics.CreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffListView(generics.ListCreateAPIView):
    serializer_class = StaffSerializer

    def get_queryset(self):
        return Staff.objects.filter(company__user=self.request.user)

class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StaffSerializer

    def get_queryset(self):
        return Staff.objects.filter(company__user=self.request.user)




#----------------View for Employee --------------------------
class EmployeeCreateView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(company__user=self.request.user)
    
class EmployeeListView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(company__user=self.request.user)

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(company__user=self.request.user)
    


#--------------View for asset------------------

class AssetCreateView(generics.CreateAPIView):
    serializer_class = AssetSerializer

    def get_queryset(self):
        return Asset.objects.filter(company__user=self.request.user)

class AssetListView(generics.ListCreateAPIView):
    serializer_class = AssetSerializer

    def get_queryset(self):
        return Asset.objects.filter(company__user=self.request.user)

class AssetDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer

    def get_queryset(self):
        return Asset.objects.filter(company__user=self.request.user)




#--------------View for assetlog------------------


class AssetLogCreateView(generics.CreateAPIView):
    serializer_class = AssetLogSerializer

    def get_queryset(self):
        return AssetLog.objects.filter(company__user=self.request.user)
    
class AssetLogUpdateView(generics.UpdateAPIView):#updating assets log
    serializer_class = AssetLogSerializer

    def get_queryset(self):
        return AssetLog.objects.filter(company__user=self.request.user)
class AssetLogListView(generics.ListCreateAPIView):
    serializer_class = AssetLogSerializer

    def get_queryset(self):
        return AssetLog.objects.filter(company__user=self.request.user)

class AssetLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetLogSerializer

    def get_queryset(self):
        return AssetLog.objects.filter(company__user=self.request.user)



#---------------Optional View for company---------------

class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    

#----------registration View----------------

@permission_classes([AllowAny])
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully.", "user_id": user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email') #Login by email
        password = request.data.get('password')

        User = get_user_model()
        try:
            user = User.objects.get(email=email) 
        except User.DoesNotExist:
            return Response({"message": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if user is not None and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({"access_token": access_token}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
@permission_classes([AllowAny])
class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        return response
    