"""adminpos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from accounts.forms import CustomLoginForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('salesinvoice/',include('sales.urls')),
    path('purchaseinvoice/',include('purchase.urls')),
    path('accounts/login/',LoginView.as_view(template_name='AdminPos/login.html',form_class=CustomLoginForm),name='login'),
    path('accounts/logout/',LogoutView.as_view(),name='logout'),
    path('products/',include('products.urls')),
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

