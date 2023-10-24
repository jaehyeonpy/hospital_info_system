"""
URL configuration for hospital_info_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg import openapi
from rest_framework import permissions

from django.urls import include, path
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
      title="hospital_info_system API document",
      default_version='V0.1',
      contact=openapi.Contact(email="jaehyeonpy@gmail.com"),
      license=openapi.License(name="MIT"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('hospital_info_applyer.urls')),
    path('swagger/', schema_view.with_ui('swagger')),
]
