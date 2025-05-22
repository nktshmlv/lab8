from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calls/', include('calls.urls')),
    path('', lambda request: redirect('call_list')),
]