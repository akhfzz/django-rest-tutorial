from django.contrib import admin
from django.urls import path
from .views import APIMahasiswa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', APIMahasiswa.as_view()),
    path('user/<int:id>', APIMahasiswa.as_view())
]