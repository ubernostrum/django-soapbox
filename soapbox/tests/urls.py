from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
                       (r'^$', direct_to_template,
                        {'template': 'soapboxtest/test_success.html'}),
                       (r'^foo/$', direct_to_template,
                        {'template': 'soapboxtest/test_success.html'}),
                       (r'^foo/bar/$', direct_to_template,
                        {'template': 'soapboxtest/test_success.html'}),
                       (r'^fail/$', direct_to_template,
                        {'template': 'soapboxtest/test_fail_syntax.html'}),
)
