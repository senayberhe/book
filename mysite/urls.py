from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #user management 
    # path('accounts/', include('django.contrib.auth.urls')),
    #local apps 
    path('', include('allauth.urls')),
    path('', include('pages.urls')),
    path('books/', include('books.urls')),
    path('orders/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
