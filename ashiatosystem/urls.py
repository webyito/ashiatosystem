"""ashiato_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rakucad/', include('rakucad.urls')),
    path('base/', include('base.urls')),
    path('rakucad_2022_10/', include('rakucad_2022_10.urls')),
    path('webchalle_estate/', include('webchalle_estate.urls')),
    path('webchalle_salon/', include('webchalle_salon.urls')),
    path('webchalle_gourmet/', include('webchalle_gourmet.urls')),
    path('car/', include('car.urls')),
    path('rakucad_2023_02/',include('rakucad_2023_02.urls')),
    path('demo/', include('demo.urls')),
    path('sanei_uranus/', include('sanei_uranus.urls')),
    path('testito/',include('testito.urls')),
]