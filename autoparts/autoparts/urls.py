from functools import partial

from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf.urls.static import static

static_routes = ['shop', 'home', 'cart']

static_patterns = [
    re_path(r'^{0}/.*$'.format(route), TemplateView.as_view(template_name='index.html')) for route in static_routes
]


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += static_patterns

print(settings.STATIC_DIR)
# То что ниже не должно работать в проде. За раздачу статики должен отвечать nginx или apache
if settings.DEBUG or settings.SERVE_STATIC:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static("swagger/static/", document_root=settings.STATIC_ROOT)
    urlpatterns += [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "swagger/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path(
            "favicon.ico",
            partial(serve, path="logo.png", document_root=settings.STATIC_DIR),
        ),
    ]
