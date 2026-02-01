"""URL configuration for the backend."""
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def _health_check(request):
    return JsonResponse({'status': 'ok'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', _health_check, name='health'),
]
