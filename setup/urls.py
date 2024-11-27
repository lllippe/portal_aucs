from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('portal_aucs.urls')),
    path('', include('pontos.urls')),
    path('admin/', admin.site.urls),
]
