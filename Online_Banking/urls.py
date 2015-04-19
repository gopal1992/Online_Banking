from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/', 'Online_Services.views.home'),
    url(r'^login/', 'Online_Services.views.login'),
    url(r'^sign_up/', 'Online_Services.views.sign_up'),
    url(r'^sign_up_user/', 'Online_Services.views.sign_up_user'),
    # Examples:
    # url(r'^$', 'Online_Banking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
