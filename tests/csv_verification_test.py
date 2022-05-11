import os

from flask_login import FlaskLoginClient

from app import db
from app.db.models import User


def test_csv_upload_and_verification(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    user = User.query.get(1)

    assert db.session.query(User).count() == 1
    assert user.email == 'keith@webizly.com'

    with application.test_client(user=None) as client:
        # This request has no user logged in, so they can not access the page.
        response = client.get('/songs/upload')
        assert response.status_code == 302

    with application.test_client(user=user) as client:
        # This request already has a user logged in, so they can access the page.
        response = client.get('/songs/upload')
        assert response.status_code == 200

        # Checking to see that csv submits and validates.
        root = os.path.dirname(os.path.abspath(__file__))
        music_csv = os.path.join(root, '../sample_csv/music.csv')
        music_csv_data = open(music_csv, 'rb')
        data = {'file': (music_csv_data, 'music.csv')}

        response = client.post('/songs/upload', data=data)
        assert response.status_code == 302
        assert response.headers["Location"] == "/songs"
