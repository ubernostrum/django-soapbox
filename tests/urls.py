from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="soapboxtest/test_success.html")),
    path("foo/", TemplateView.as_view(template_name="soapboxtest/test_success.html")),
    path(
        "foo/bar/",
        TemplateView.as_view(template_name="soapboxtest/test_success.html"),
    ),
    path(
        "foo/bar/baz/",
        TemplateView.as_view(template_name="soapboxtest/test_context_processor.html"),
    ),
    path(
        "fail/",
        TemplateView.as_view(template_name="soapboxtest/test_fail_syntax.html"),
    ),
    path(
        "bad-url-var/",
        TemplateView.as_view(template_name="soapboxtest/test_bad_variable.html"),
    ),
]
