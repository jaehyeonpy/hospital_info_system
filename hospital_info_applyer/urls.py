from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'hospital', views.HospitalViewSet)
router.register(r'doctor', views.DoctorViewSet)
router.register(r'school', views.SchoolViewSet)
router.register(r'major', views.MajorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]