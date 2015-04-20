import os

from setuptools import setup


setup(name='django-soapbox',
      version='1.1',
      description='Site-wide and page-specific announcements/messages for Django sites',
      long_description=open(os.path.join(os.path.dirname(__file__), 'README')).read(),
      author='James Bennett',
      author_email='james@b-list.org',
      url='https://github.com/ubernostrum/django-soapbox',
      download_url='http://static.b-list.org//files/django-soapbox-1.0.tar.gz', 
      packages=['soapbox', 'soapbox.templatetags', 'soapbox.tests', 'soapbox.templates'],
      package_dir={'soapbox': 'soapbox'},
      package_data={'soapbox': ['templates/soapboxtest/*.html']},
      test_suite='soapbox.runtests.run_tests',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Framework :: Django :: 1.7',
                   'Framework :: Django :: 1.8',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Utilities'],
      )
