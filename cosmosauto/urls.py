from django.urls import path
from cosmosauto import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('redirect', views.RedirectView.as_view(), name='redirect')
]