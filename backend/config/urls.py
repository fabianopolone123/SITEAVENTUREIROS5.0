from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

from backend.ui import urls as ui_urls


def health_view(request):
    return HttpResponse("OK", content_type="text/plain")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(ui_urls)),
    path("health/", health_view, name="health"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
