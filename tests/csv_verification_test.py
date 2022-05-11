import os

from flask_login import FlaskLoginClient

from app import db
from app.db.models import User, Transactions


def test_csv_upload_and_verification(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    user = User.query.get(1)
    transactions = Transactions.query.get(1)

    assert transactions is None
    assert db.session.query(User).count() == 1
    assert user.email == 'keith@webizly.com'

    with application.test_client(user=None) as client:
        # This request has no user logged in, so they can not access the page.
        response = client.get('/transactions/upload')
        assert response.status_code == 302

    with application.test_client(user=user) as client:
        # This request already has a user logged in, so they can access the page.
        response = client.get('/transactions/upload')
        assert response.status_code == 200

        # Checking to see that csv submits and validates.
        root = os.path.dirname(os.path.abspath(__file__))
        transactions_csv = os.path.join(root, '../sample_csv/transactions.csv')
        transactions_csv_data = open(transactions_csv, 'rb')
        data = {'file': (transactions_csv_data, 'transactions.csv')}

        # Balance should be 0 before the upload.
        assert user.balance == 0

        response = client.post('/transactions/upload', data=data)

        # Balance should be the sum of all amounts after upload.
        assert user.balance == 10601

        # Proper redirect test.
        assert response.status_code == 302
        assert response.headers["Location"] == "/transactions"
