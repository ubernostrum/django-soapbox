from django.conf.urls import patterns
from django.views.generic import TemplateView


urlpatterns = patterns('',
    (r'^$',
     TemplateView.as_view(
         template_name='soapboxtest/test_success.html'
     )),
    (r'^foo/$',
     TemplateView.as_view(
         template_name='soapboxtest/test_success.html'
     )),
    (r'^foo/bar/$',
     TemplateView.as_view(
         template_name='soapboxtest/test_success.html'
     )),
    (r'^fail/$',
     TemplateView.as_view(
         template_name='soapboxtest/test_fail_syntax.html'
     )),
)
