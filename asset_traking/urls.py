
from django.urls import path
from .views import SignupView, LoginView, MyTokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

urlpatterns = [
   
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('signup/', SignupView.as_view(), name='signup'),#This is for general signup
    path('login/', LoginView.as_view(), name='login'),
    
    path('signup-as-company-owner', views.CompanyCreateView.as_view(), name='company-create'),
    path('signup-as-staff/', views.StaffCreateView.as_view(), name='staff-create'),
    

    path('companies/', views.CompanyListView.as_view(), name='company-list'),
    path('companies/<int:pk>/', views.CompanyDetailView.as_view(), name='company-detail'),

    # Staff
    path('staff/', views.StaffListView.as_view(), name='staff-list'),
    path('staff/<int:pk>/', views.StaffDetailView.as_view(), name='staff-detail'),

    # Employees
    path('employees/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee-create'),
    
    # Assets
    path('assets/', views.AssetListView.as_view(), name='asset-list'),
    path('assets/<int:pk>/', views.AssetDetailView.as_view(), name='asset-detail'),
    path('assets/create/', views.AssetCreateView.as_view(), name='asset-create'),
    
    # Asset Logs
    path('asset-logs/', views.AssetLogListView.as_view(), name='assetlog-list'),
    path('asset-logs/<int:pk>/', views.AssetLogDetailView.as_view(), name='assetlog-detail'),
    path('asset-logs/create/', views.AssetLogCreateView.as_view(), name='assetlog-create'),
    path('assetlog/<int:pk>/update/', views.AssetLogUpdateView.as_view(), name='assetlog-update'),


    
    
    
]

