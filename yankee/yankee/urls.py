"""yankee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views, settings
from django.conf.urls import url, handler403, handler404, handler500

# handler403 = 'IQRA.views.error_403'
# handler404= 'IQRA.views.error_404'
# handler500= 'IQRA.views.error_500'
from django.conf.urls.static import static

urlpatterns = [
    #Home Page Redirection url
    path('', views.index, name='index'),
    
    #Admin Page
    path('admin/', admin.site.urls),
    #Http error status Raise
    # path('ABMtech/WebUI/Access-Denied/', views.error_403, name='error_403'),
    # path('ABMtech/WebUI/Not-Found/', views.error_404, name='error_404'),
    # path('ABMtech/WebUI/Server-Error/', views.error_500, name='error_500'),
    
   


]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)