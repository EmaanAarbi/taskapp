from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mytasks/', include('mytasks.urls')),
    path('admin/', admin.site.urls),
    
]