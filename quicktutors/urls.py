"""quicktutors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import django.contrib.auth.views
from django.contrib import admin
from django.views.generic.base import RedirectView
from . import settings

admin.autodiscover()

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/logout$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/home'}),
    url(r'', include('quicktutorsApp.urls')),
    url(r'^user/', include('user_profile.urls')),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    url(r'^ajax_select/', include('ajax_select.urls')),
    url(r'^secciones/', include('monitorias.urls', namespace='monitorias', app_name='monitorias')),
    url('^questions/', include('quickfireQuestions.urls', namespace='quickfireQuestions', app_name='quickfireQuestions')),
    url(r'^favicon\.ico$', favicon_view),

]
