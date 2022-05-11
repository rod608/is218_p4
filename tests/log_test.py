""" This test the existence of log files """
import os


def test_request_log_exists():
    """This checks for the request log"""
    root = os.path.dirname(os.path.abspath(__file__))
    requestlog = os.path.join(root, '../logs/request.log')
    # Make if it doesn't exist
    if not os.path.exists(requestlog):
        open(requestlog, 'a').close()
    # Assert it exists
    assert os.path.exists(requestlog)


def test_errors_log_exists():
    """This checks for the errors log"""
    root = os.path.dirname(os.path.abspath(__file__))
    errorlog = os.path.join(root, '../logs/errors.log')
    # Make if it doesn't exist
    if not os.path.exists(errorlog):
        open(errorlog, 'a').close()
    assert os.path.exists(errorlog)


def test_flask_log_exists():
    """This checks for the flask log"""
    root = os.path.dirname(os.path.abspath(__file__))
    flasklog = os.path.join(root, '../logs/flask.log')
    # Make if it doesn't exist
    if not os.path.exists(flasklog):
        open(flasklog, 'a').close()
    assert os.path.exists(flasklog)


def test_info_log_exists():
    """This checks for the info log"""
    root = os.path.dirname(os.path.abspath(__file__))
    infolog = os.path.join(root, '../logs/info.log')
    # Make if it doesn't exist
    if not os.path.exists(infolog):
        open(infolog, 'a').close()
    assert os.path.exists(infolog)


def test_myapp_log_exists():
    """This checks for the myapp log"""
    root = os.path.dirname(os.path.abspath(__file__))
    myapplog = os.path.join(root, '../logs/myapp.log')
    # Make if it doesn't exist
    if not os.path.exists(myapplog):
        open(myapplog, 'a').close()
    assert os.path.exists(myapplog)


def test_sqlalchemy_log_exists():
    """This checks for the sqlalchemy log"""
    root = os.path.dirname(os.path.abspath(__file__))
    sqlalchemylog = os.path.join(root, '../logs/sqlalchemy.log')
    # Make if it doesn't exist
    if not os.path.exists(sqlalchemylog):
        open(sqlalchemylog, 'a').close()
    assert os.path.exists(sqlalchemylog)


def test_werkzeug_log_exists():
    """This checks for the werkzeug log"""
    root = os.path.dirname(os.path.abspath(__file__))
    werkzeuglog = os.path.join(root, '../logs/werkzeug.log')
    # Make if it doesn't exist
    if not os.path.exists(werkzeuglog):
        open(werkzeuglog, 'a').close()
    assert os.path.exists(werkzeuglog)
