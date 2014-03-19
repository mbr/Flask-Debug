import pytest
from flask import Flask
from flask_debug import Debug


@pytest.fixture
def app():
    app = Flask(__name__)
    Debug(app)
    app.config['DEBUG'] = True
    app.config['TESTING'] = True

    assert app.debug
    assert app.testing
    return app


@pytest.yield_fixture
def client(app):
    with app.app_context():
        yield app.test_client()


def test_works_in_debug_mode(client):
    # redirect
    assert client.get('/_debug/').status_code == 302

    assert client.get('/_reflect/').status_code == 200
    assert client.get('/_config/').status_code == 200


def test_refuses_outside_debug_mode(app, client):
    app.config['DEBUG'] = False

    # redirect
    assert client.get('/_debug/').status_code == 403

    assert client.get('/_reflect/').status_code == 403
    assert client.get('/_config/').status_code == 403
