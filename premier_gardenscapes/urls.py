"""
Project-level URL configuration for Premier Gardenscapes.
Defines the main routing and includes app-specific URLs.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.loader import render_to_string

urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),
    
    # Main website app
    path('', include('main.urls')),
    
    # SEO and web standards
    path('robots.txt', lambda request: HttpResponse(
        render_to_string('robots.txt', content_type='text/plain')
    )),
    
    path('sitemap.xml', lambda request: HttpResponse(
        render_to_string('sitemap.xml', content_type='application/xml')
    )),
]
