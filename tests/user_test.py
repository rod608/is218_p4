from app import db
from app.db.models import User, Transactions


def test_adding_user(application):
    with application.app_context():
        # assert db.session.query(User).count() == 0
        user_count = db.session.query(User).count()
        transaction_count = db.session.query(Transactions).count()

        # record creation, addition, and commit
        user = User('keith@webizly.com', 'testtest', True)
        db.session.add(user)
        db.session.commit()

        # assert that we now have a new user with no balance
        assert db.session.query(User).count() == user_count + 1
        assert user.balance == 0

        # finding user via email
        user = User.query.filter_by(email='keith@webizly.com').first()
        assert user.email == 'keith@webizly.com'

        # Adding user transactions
        user.transactions = [Transactions("200", "CREDIT"), Transactions("2000", "CREDIT")]
        db.session.commit()
        assert db.session.query(Transactions).count() == transaction_count + 2

        # Checking transaction changes #1
        transaction1 = Transactions.query.filter_by(type='CREDIT').first()
        assert transaction1.type == "CREDIT"
        transaction1.amount = "200"
        db.session.commit()

        # Checking transaction changes #2
        transaction2 = Transactions.query.filter_by(amount='2000').first()
        assert transaction2.type == "CREDIT"

        # checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == user_count
        assert db.session.query(Transactions).count() == transaction_count
