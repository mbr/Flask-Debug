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

First, create a package named ``flask_debug_yourname``. The prefix
``flask_debug_`` is important here. Here is a sample ``__init__.py`` from a
package like that::

  # file: flask_debug_myext

  # if you set a variable ``template_folder``, templates will be available
  # from the folder ``flask_debug_myext/templates``.
  template_folder = 'templates'

  # this is the central hook, the following function (which must be named
  # exactly as it is below) will be called with the Flask-Debug blueprint
  # as a parameter
  def initialize_debug_ext(dbg):

    # the route function will automatically add routes to the flask-debug menu
    # to suppress this behavior, add an argument of ``menu_name=None``
    # it's a good convention to start with an underscore + your extension name
    # to avoid conflicts
    @dbg.route('/_myext/status')
    def debug_list_extensions():
        # by convention, views in plugins should start with ``debug_``

        status = 'all good'

        # this will render ``flask_debug_myext/templates/myext/status.html``
        # template namespace is global, therefore we use folders here as a
        # namespace
        return render_template('myext/status.html', status=status)

Using <a href="http://getboostrap.com">Bootstrap</a> (without depending on
<a href="http://pypi.python.org/pypi/Flask-Bootstrap">Flask-Bootstrap</a>,
to keep the installed code small), Flask-Debug ships a few base templates
which you can then use::

  {% extends "flask_debug/base.html" %}

  {% block content %}
  {{super()}}
  <h1>Status for myext</h1>
  <p>Current status: {{status}}</p>
  {% endblock %}
