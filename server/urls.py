
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('userauth.urls')),
    path('user/', include('cart.urls')),
    path('products/', include('product.urls')),
    path('newsletter', include('newsletter.urls'))
]
