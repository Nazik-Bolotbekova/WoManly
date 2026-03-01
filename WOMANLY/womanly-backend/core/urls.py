
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

def about_us(request):
    return render(request=request,template_name='about_us.html')

def index(request):
    return render(request=request,template_name='index.html')


urlpatterns = [
    path('',index,name='index'),
    path('admin/', admin.site.urls),
    path('content/',include('apps.content.urls')),
    path('users/',include('apps.users.urls')),
    path('about_us/',about_us),
    path('accounts/',include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

