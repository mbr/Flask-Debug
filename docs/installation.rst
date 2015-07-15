Installing and instantiating
============================

First, Flask-Debug must be installed from PyPI <http://pypi.python/org/pypi
/Flask-Debug>`_:

.. code-block:: shell

    $ pip install flask-debug



Flask-AppConfig
---------------

`flask-appconfig>=0.10 <https://github.com/mbr/flask-appconfig>`_ supports
automatic initialization of Flask-Debug while developing, allowing you to
completely omit it from your own code (and therefore production deployments).
See the Flask-AppConfig docs for details.


Security
--------

**Never enable ``debug`` on a production server** (the configuration
variable, the extension is safe to use in production,
as it will simply refuse everything when the app is not running with
debugging enabled). This is Flask basic practice (see
http://flask.pocoo.org/docs/quickstart/#debug-mode). Flask-Debug tries to
prevent security disasters if you forget to disable debugging in production,
but please, don't!
