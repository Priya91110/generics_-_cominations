from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car_data/',views.CarListCreateView.as_view()),
    path('car_detail/<int:pk>/',views.CarDetailView.as_view()),
    
]