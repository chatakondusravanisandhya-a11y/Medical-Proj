"""
URL configuration for hospital_management project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Customize admin site
admin.site.site_header = "Arogya Medical Center Administration"
admin.site.site_title = "Arogya Admin"
admin.site.index_title = "Welcome to Arogya Medical Center Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital_system.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
