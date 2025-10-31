from django.urls import path, include

urlpatterns = [
    path('api/cars/', include('cars.urls')),  # or similar
]