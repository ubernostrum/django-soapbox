.. _install:


Installation guide
==================

Before installing django-soapbox, you'll need to have a copy
of `Django <https://www.djangoproject.com>`_ already installed. For
information on obtaining and installing Django, consult the `Django
download page <https://www.djangoproject.com/download/>`_, which
offers convenient packaged downloads and installation instructions.

The |version| release of django-soapbox is supports Django 1.11, 2.2, and 3.0 on
supported version of Python 3.

* Django 1.11 supports Python 3.5, 3.6, 3.7, and 3.8

* Django 2.2 supports Python 3.5, 3.6, 3.7, and 3.8

* Django 3.0 supports Python 3.6, 3.7, and 3.8


Normal installation
-------------------

The preferred method of installing django-soapbox is via ``pip``,
the standard Python package-installation tool. If you don't have
``pip``, instructions are available for `how to obtain and install it
<https://pip.pypa.io/en/latest/installing.html>`_. If you're using
Python 2.7.9 or later (for Python 2) or Python 3.4 or later (for
Python 3), ``pip`` came bundled with your installation of Python.

Once you have ``pip``, type::

    pip install django-soapbox


Installing from a source checkout
---------------------------------

If you want to work on django-soapbox, you can obtain a source
checkout.

The development repository for django-soapbox is at
<https://github.com/ubernostrum/django-soapbox>. If you have `git
<http://git-scm.com/>`_ installed, you can obtain a copy of the
repository by typing::

    git clone https://github.com/ubernostrum/django-soapbox.git

From there, you can use normal git commands to check out the specific
revision you want, and install it using ``pip install -e .`` (the
``-e`` flag specifies an "editable" install, allowing you to change
code as you work on django-soapbox, and have your changes picked
up automatically).


Configuration and use
---------------------

Once you have Django and django-soapbox installed, check out :ref:`the
usage overview <overview>` to see how to start using messages on your
site.
