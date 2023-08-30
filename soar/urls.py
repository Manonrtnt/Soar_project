from django.urls import path
from .views import CaptureRequestView, LoginView, CaptureRequestSuccessView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', CaptureRequestView.as_view(), name='capture_request'),
    path('capture_request_success/', CaptureRequestSuccessView.as_view(), name='capture_request_success'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]