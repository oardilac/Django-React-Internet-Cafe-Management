from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cyber.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)