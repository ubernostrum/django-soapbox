from distutils.core import setup
import os


setup(name='django-soapbox',
      version='1.0',
      description='Site-wide and page-specific announcements/messages for Django sites',
      long_description=open(os.path.join(os.path.dirname(__file__), 'README')).read(),
      author='James Bennett',
      author_email='james@b-list.org',
      url='https://github.com/ubernostrum/django-soapbox',
      download_url='http://static.b-list.org//files/django-soapbox-1.0.tar.gz', 
      packages=['soapbox', 'soapbox.templatetags', 'soapbox.tests', 'soapbox.templates'],
      package_dir={'soapbox': 'soapbox'},
      package_data={'soapbox': ['templates/soapboxtest/*.html']},
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
