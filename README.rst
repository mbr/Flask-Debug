Flask-Debug
===========

Flask-Debug is an extension for Flask_ that displays various debugging insights
during development.

.. code-block:: python

    from flask import Flask
    from flask_debug import Debug

    app = Flask(__name__)
    Debug(app)
    app.run(debug=True)


It can be manually added but also (using Flask-Appconfig_) be
automatically instantiated only during development and invisible in production.

Opening http://localhost:5000/_debug will show some information about the
application, such as a list of registered views, url maps or configuration
values.

See the `documentation <http://pythonhosted.org/Flask-Debug>`_ for more
details.
