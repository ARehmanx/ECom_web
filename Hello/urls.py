from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "T-Point Admin Login"
admin.site.site_title = "T-Point Admin Portal"
admin.site.index_title = "Welcome to T-Point"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('home.urls')),
    path('/conatct/', include('home.urls'))
]