from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^$',
        TemplateView.as_view(
            template_name='soapboxtest/test_success.html')),
    url(r'^foo/$',
        TemplateView.as_view(
            template_name='soapboxtest/test_success.html')),
    url(r'^foo/bar/$',
        TemplateView.as_view(
            template_name='soapboxtest/test_success.html')),
    url(r'^foo/bar/baz/$',
        TemplateView.as_view(
            template_name='soapboxtest/test_context_processor.html')),
    url(r'^fail/$',
        TemplateView.as_view(
            template_name='soapboxtest/test_fail_syntax.html')),
    url(r'^bad-url-var/$',
        TemplateView.as_view(
            template_name='soapboxtest/test_bad_variable.html')),
)
