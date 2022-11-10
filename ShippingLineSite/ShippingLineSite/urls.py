from django.contrib import admin
from django.urls import path, include
from django_backend import views
from rest_framework.routers import DefaultRouter


from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.getRoutes),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

