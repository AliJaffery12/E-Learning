"""video_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

from django.urls import path,include

urlpatterns = [
    path('',views.Homepage,name='home'),
    path('admin/', admin.site.urls),
    path('courses/',include('courses.urls',namespace='courses')),
    path('memberships/',include('memberships.urls',namespace='memberships')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('quiz/', include('quiz.urls')),
   # path('quizes/',include('quizes.urls',namespace='quiz')),
   
    path('search/',views.Search,name='search'),
    path('test/',views.TestPage.as_view(),name='test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
    path('contact/',views.Contactpage,name='contact'),
    path('about/',views.AboutPage,name='about'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)