
from django.contrib import admin
from django.urls import path
from useragent_middleware import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.demo, name='index'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
