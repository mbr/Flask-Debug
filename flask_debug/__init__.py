from functools import wraps

from flask import current_app, render_template, Blueprint, abort, url_for, redirect


dbg = Blueprint('debug', __name__, template_folder='templates')


def requires_debug(view):
    @wraps(view)
    def _(*args, **kwargs):
        if not current_app.debug:
            abort(403, 'This function is only available if the application '
                       'has been started in debug mode.')
        return view(*args, **kwargs)
    return _


@dbg.route('/_debug/')  # the root
@requires_debug
def debug_root():
    return redirect(url_for('.debug_reflect'))


@dbg.route('/_reflect/')
@requires_debug
def debug_reflect():
    return render_template(
        'debug_reflect.html',
        app=current_app,
    )


@dbg.route('/_config/')
@requires_debug
def debug_config():
    return render_template(
        'debug_config.html',
        app=current_app,
    )


class Debug(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(dbg)
