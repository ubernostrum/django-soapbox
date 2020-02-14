import os

from setuptools import setup


setup(name='django-soapbox',
      version='1.5',
      zip_safe=False,  # eggs are the devil.
      description=("Site-wide and page-specific announcements/messages for "
                   "Django sites"),
      long_description=open(
          os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
      author='James Bennett',
      author_email='james@b-list.org',
      url='https://github.com/ubernostrum/django-soapbox',
      packages=['soapbox', 'soapbox.templatetags', 'soapbox.migrations',
                'soapbox.tests', 'soapbox.tests.templates'],
      package_dir={'soapbox': 'soapbox'},
      package_data={'soapbox': ['tests/templates/soapboxtest/*.html']},
      test_suite='soapbox.runtests.run_tests',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Framework :: Django :: 1.11',
                   'Framework :: Django :: 2.2',
                   'Framework :: Django :: 3.0',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Topic :: Utilities'],
      install_requires=[
          'Django>=1.11',
      ],
)
