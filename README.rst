Flask-Debug
===========

.. image:: https://travis-ci.org/mbr/Flask-Debug.png?branch=master   :target: https://travis-ci.org/mbr/Flask-Debug

Flask-Debug is a simple WIP Flask-extension, intended solely for development.
Example usage::

  from flask import Flask
  from flask_debug import Debug
  app = Flask(__name__)
  Debug(app)
  app.run(debug=True)

Now opening http://localhost:5000/_debug will show some information about
the application, such as a list of registered views,
url maps or configuration values.


Security
--------

Of course, this should never be enabled on a production server. If the
application is not running in debug mode, the extension will refuse any
interaction with the outside world.
