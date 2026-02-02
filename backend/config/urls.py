from django.http import HttpResponse
from django.urls import include, path

from backend.ui import urls as ui_urls


def health_view(request):
    return HttpResponse("OK", content_type="text/plain")


urlpatterns = [
    path("", include(ui_urls)),
    path("health/", health_view, name="health"),
]
