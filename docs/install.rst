.. _install:


Installation guide
==================

The |release| release of django-soapbox supports Django 3.2, 4.1 and
4.2 on the following Python versions:

* Django 3.2 supports Python 3.8, 3.9, and 3.10.

* Django 4.1 supports Python 3.8, 3.9, 3.10 and 3.11.

* Django 4.2 supports Python 3.8, 3.9, 3.10 and 3.11.

Normal installation
-------------------

The preferred method of installing django-soapbox is via `pip`,
the standard Python package-installation tool. If you don't have
`pip`, instructions are available for `how to obtain and install it
<https://pip.pypa.io/en/latest/installing.html>`_, though if you're
using a supported version of Python, `pip` should have come bundled
with your installation of Python.

Once you have `pip`, type::

    pip install django-soapbox

If you don't have a copy of a compatible version of Django, this will
also automatically install one for you.


Installing from a source checkout
---------------------------------

If you want to work on django-soapbox, you can obtain a source
checkout.

The development repository for django-soapbox is at
<https://github.com/ubernostrum/django-soapbox>. If you have `git
<http://git-scm.com/>`_ installed, you can obtain a copy of the
repository by typing::

    git clone https://github.com/ubernostrum/django-soapbox.git

From there, you can use git commands to check out the specific
revision you want, and perform an "editable" install (allowing you to
change code as you work on it) by typing::

    pip install -e .


Next steps
----------

To learn how to use django-soapbox, see :ref:`the usage overview <overview>`.