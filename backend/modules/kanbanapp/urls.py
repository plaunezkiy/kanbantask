from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('cards', views.CardViewSet, basename='cards')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/resort/', views.resortCards, name='cards_resort'),
    path('auth/google/', views.GoogleLogin.as_view(), name='google_login'),
]
