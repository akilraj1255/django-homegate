Django Homegate
============

django-homegate provides IDX3.01 API support for your Django project by closing the gap between python-homegate (https://github.com/arteria/python-homegate) and your Django real estate Django app.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install django-homegate

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/arteria/django-homegate.git#egg=django_homegate

TODO: Describe further installation steps (edit / remove the examples below):

Add ``django_homegate`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'django_homegate',
    )

Add the ``django_homegate`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^homegate/', include('django_homegate.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load django_homegate_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate django_homegate


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-homegate
    $ python setup.py install
    $ pip install -r dev_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
