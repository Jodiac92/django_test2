"""django_test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from gpapp import views
from gpapp.views import CallView
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.MainFunc, name='MainFunc'), # 방법1 Function views
    path('gpapp/callget', CallView.as_view()),  # 방법2 Class-based views
    path('gpapp/', include('gpapp.urls')),  #방법3 Including another URLconf (권장)
]



