"""
URL configuration for the main app.
Defines the routing for the Premier Gardenscapes website.
"""

from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # Main landing page - single page with all sections
    path('', views.home, name='home'),
]
