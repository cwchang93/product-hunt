
from django.contrib import admin
from django.urls import path, include
from products import views
#從product app中引入view的模組！


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('accounts/', include('accounts.urls')),
]
