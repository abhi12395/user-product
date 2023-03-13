from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from product.views import*



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('product/', include('product.urls')),
]
