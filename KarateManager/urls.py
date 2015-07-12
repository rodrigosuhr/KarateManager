from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'KarateManager.views.home'),
    url(r'^payments/', include('payments.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
