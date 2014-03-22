Flask-Debug
===========

.. image:: https://travis-ci.org/mbr/Flask-Debug.svg?branch=master
   :target: https://travis-ci.org/mbr/Flask-Debug

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


Writing your own plugins
------------------------

It's fairly easy to ship a plugin for Flask-Debug with your own package or
Flask-extension. This allows you to ship debugging tools right along with
the extension.

First, create a package named ``flask_debug_yourname``, the prefix
``flask_debug_`` is important. Your ``__init__.py`` should look somewhat
like this::

  # file: flask_debug_myext/__init__.py

  template_folder = 'templates'

  def initialize_debug_ext(dbg):
      @dbg.route('/_myext/status')
      def debug_list_extensions():
          status = 'all good'

          return render_template('myext/status.html', status=status)

``initialize_debug_ext()`` will be called with a ``flask.Blueprint``-Object
as the first parameter, onto which you can register your own routes. The
``route()`` function will automatically a menu entry (to suppress this
behavior, add an argument of ``menu_name=None``).

There are a few conventions:

* Views in plugins should start with ``debug_``.
* URLs in routes should start with underscore + your extension name.
* Inside your ``templates``-folder, you should also create subfolder named ``myext``
  for all of your templates, as the template namespace is global.

Using `Bootstrap <http://getboostrap.com>`_, Flask-Debug ships a few base
templates which you can use::

  {# file: flask_debug_myext/templates/myext/status.html #}
  {% extends "flask_debug/base.html" %}

  {% block content %}
  {{super()}}
  <h1>Status for myext</h1>
  <p>Current status: {{status}}</p>
  {% endblock %}

To finally load the plugin, just do::

  import flask_debug_myext

in your extension. Before registering the debugging-blueprint onto the app,
Flask-Debug will query ``sys.modules`` for all modules that look like
Flask-Debug plugins and collect them.

You can check out the ``flask_debug_plugins``-plugin (which lists all
installed plugins) for an example.
