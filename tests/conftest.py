"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
import logging
import os

import pytest
from app import create_app, User
from app.db import db
from flask import current_app


# this is a good tutorial I used to fix this code to do database testing.
# https://xvrdm.github.io/2017/07/03/testing-flask-sqlalchemy-database-with-pytest/


@pytest.fixture()
def application():
    """This makes the app"""
    # you need this one if you want to see whats in the database
    # os.environ['FLASK_ENV'] = 'development'
    # you need to run it in testing to pass on github
    os.environ['FLASK_ENV'] = 'testing'

    application = create_app()

    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        # drops the database tables after the test runs
        db.drop_all()


@pytest.fixture()
def add_user(application):
    with application.app_context():
        # new record
        user = User('keith@webizly.com', 'testtest', True, 0)
        db.session.add(user)
        db.session.commit()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='jimmy1945@joe.com', password='jimmy1941'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
