from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    path('', TemplateView.as_view(template_name="base/index.html"), name='home'),
     path('admin/', admin.site.urls),
     # allauth for  login with google urls 
    path('accounts/', include('allauth.urls')),
]