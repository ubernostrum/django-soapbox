"""
A standalone test runner script, configuring the minimum settings
required for django-soapbox's tests to execute.

Re-use at your own risk: many Django applications will require a more
extensive list of settings.

"""

import os
import sys


# Make sure django-soapbox is (at least temporarily) on the import
# path.
SOAPBOX_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, SOAPBOX_DIR)


# Minimum settings required to test django-soapbox.
SETTINGS_DICT = {
    'INSTALLED_APPS': ('soapbox',),
    'ROOT_URLCONF': 'soapbox.tests.urls',
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(SOAPBOX_DIR, 'db.sqlite3'),
        },
    },
    'MIDDLEWARE_CLASSES': (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
    ),
    'TEMPLATE_LOADERS': (
        'django.template.loaders.app_directories.Loader',
    ),
    'TEMPLATE_CONTEXT_PROCESSORS': (
        'django.core.context_processors.request',
    ),
}


def run_tests():
    # Making Django run this way is a two-step process. First, call
    # settings.configure() to give Django settings to work with:
    from django.conf import settings
    settings.configure(**SETTINGS_DICT)

    # Then, call django.setup() to initialize the application cache
    # and other bits:
    import django
    if hasattr(django, 'setup'):
        django.setup()

    # Now we instantiate a test runner...
    from django.test.utils import get_runner
    TestRunner = get_runner(settings)

    # And then we run tests and return the results.
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['soapbox.tests'])
    sys.exit(bool(failures))
