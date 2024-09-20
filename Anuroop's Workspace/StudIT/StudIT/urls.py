from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home_view  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Add this line for the home page
    path('', include('core.urls')),  # Include your app's URLs
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
