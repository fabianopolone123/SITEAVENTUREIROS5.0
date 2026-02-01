"""URL configuration for the backend."""
from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import path


def _health_check(request):
    return JsonResponse({'status': 'ok'})


def _home(request):
    return HttpResponse("<h1>Espaço do Clube – back-end funcionando</h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', _health_check, name='health'),
    path('', _home, name='home'),
]
