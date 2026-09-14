from django.urls import path
from .views import home, fix_admin

urlpatterns = [
    path('', home, name='home'),
    path('fix-admin-access/', fix_admin, name='fix_admin'),
]