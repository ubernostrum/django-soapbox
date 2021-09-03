"""
A standalone test runner script, configuring the minimum settings
required for tests to execute.

Re-use at your own risk: many Django applications will require
different settings and/or templates to run their tests.

"""

import os
import sys

from django.core.management.utils import get_random_secret_key
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = get_random_secret_key(50, chars)

APP_DIR = os.path.abspath(os.path.dirname(__file__))


# Minimum settings required for the app's tests.
SETTINGS_DICT = {
    "BASE_DIR": APP_DIR,
    "INSTALLED_APPS": (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
        "django.contrib.sites",
        "soapbox",
        "tests",
    ),
    "ROOT_URLCONF": "tests.urls",
    "DATABASES": {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(APP_DIR, "db.sqlite3"),
        },
    },
    "MIDDLEWARE": (
        "django.middleware.common.CommonMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
    ),
    "TEMPLATES": [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(APP_DIR, "tests/templates")],
            "OPTIONS": {
                "context_processors": [
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.request",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "soapbox.context_processors.soapbox_messages",
                ],
            },
        }
    ],
}


def run_tests():
    # Making Django run this way is a two-step process. First, call
    # settings.configure() to give Django settings to work with:
    from django.conf import settings

    settings.configure(**SETTINGS_DICT)

    # Then, call django.setup() to initialize the application cache
    # and other bits:
    import django

    django.setup()

    # Now we instantiate a test runner...
    from django.test.utils import get_runner

    TestRunner = get_runner(settings)

    # And then we run tests and return the results.
    test_runner = TestRunner(verbosity=2, interactive=True)
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))


if __name__ == "__main__":
    run_tests()
