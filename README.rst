=============================
Zinnia-url-shorterner-hashids
=============================

Zinnia-url-shortener-hashids is a package providing URL shortening within
`django-blog-zinnia`_ with non-sequential, short and unique ids.

Installation
============

* Install the package on your system: ::

  $ pip install zinnia-url-shortener-hashids

  `hashids`_ will also be installed as a dependency.

* Put this setting to enable the URL shortener backend:

  ``ZINNIA_URL_SHORTENER_BACKEND = 'zinnia_hashids'``

* Then include this URLconf into your project: ::

    url(r'^', include('zinnia_hashids.urls')),

.. _django-blog-zinnia: http://django-blog-zinnia.com
.. _hashids: https://github.com/davidaurelio/hashids-python
