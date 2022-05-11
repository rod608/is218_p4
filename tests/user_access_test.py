from app import db
from app.auth.forms import *
from flask_login import FlaskLoginClient
from app.db.models import User


# Login
def test_login_validates(application, client):
    """ Tests login w/ proper credentials. """
    form = login_form()
    form.email.data = "joebob@joe.com"
    form.password.data = "jimmy1941"
    assert form.validate()


def test_login_not_validates(application, client):
    """ Tests login w/ improper credentials. No password. """
    form = login_form()
    form.email.data = "joebob@joe.com"
    form.password.data = "12345"
    assert not form.validate()


def test_register_validates(application, client):
    """ Tests register w/ proper credentials. """
    form = register_form()
    form.email.data = "joebob@joe.com"
    form.password.data = "jimmy1941"
    form.confirm.data = "jimmy1941"
    assert form.validate()


def test_register_not_validates(application, client):
    """ Tests register w/ improper credentials. Passwords don't match. """
    form = register_form()
    form.email.data = "joebob@joe.com"
    form.password.data = "jimmy1941"
    form.confirm.data = "jimmy1942"
    assert not form.validate()


def test_dashboard_access_granted(application, client, add_user):
    """ Tests granted access to the dashboard with a user logged in. """
    application.test_client_class = FlaskLoginClient
    user = User.query.get(1)

    assert db.session.query(User).count() == 1
    assert user.email == 'keith@webizly.com'

    with application.test_client(user=user) as client:
        # This request already has a user logged in.
        response = client.get('/dashboard')
        assert b'keith@webizly.com' in response.data
        assert response.status_code == 200


def test_dashboard_access_denied(application, client):
    """ Tests denied access to the dashboard as a user isn't logged in. """
    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 0

    with application.test_client(user=None) as client:
        # This request does NOT have a user logged in.
        response = client.get('/dashboard')
        assert response.status_code != 200
        assert response.status_code == 302


def test_csv_upload_granted(application, client, add_user):
    """ Test that verifies that uploading CSV files is allowed for users. """
    application.test_client_class = FlaskLoginClient
    user = User.query.get(1)

    assert db.session.query(User).count() == 1
    assert user.email == 'keith@webizly.com'

    with application.test_client(user=user) as client:
        # This request has a user logged in.
        response = client.get('/songs/upload')
        assert response.status_code == 200


def test_csv_upload_denied(application, client):
    """ Test that verifies that uploading CSV files is denied for non-users """
    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 0

    with application.test_client(user=None) as client:
        # This request has a user logged in.
        response = client.get('/songs/upload')
        assert response.status_code != 200
        assert response.status_code == 302
