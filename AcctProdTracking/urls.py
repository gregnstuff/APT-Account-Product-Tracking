
from django.contrib import admin
from django.urls import path, include
from theme.views import change_theme

urlpatterns = [
    path('admin/', admin.site.urls),
    path('switch-theme', change_theme, name="change-theme"),
    path('', include('public.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('product/', include('product.urls')),
    path('account/', include('account.urls')),
    path('issue/', include('issue.urls')),
]
