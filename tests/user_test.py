from app import db
from app.db.models import User, Transactions


def test_adding_user(application):
    with application.app_context():
        # assert db.session.query(User).count() == 0
        user_count = db.session.query(User).count()
        transaction_count = db.session.query(Transactions).count()
        # showing how to add a record
        # create a record
        user = User('keith@webizly.com', 'testtest', True)
        # add it to get ready to be committed
        db.session.add(user)
        # call the commit
        db.session.commit()
        # assert that we now have a new user
        assert db.session.query(User).count() == user_count + 1
        # finding one user record by email
        user = User.query.filter_by(email='keith@webizly.com').first()
        # asserting that the user retrieved is correct
        assert user.email == 'keith@webizly.com'
        # this is how you get a related record ready for insert
        user.transactions = [Transactions("200", "CREDIT"), Transactions("2000", "CREDIT")]
        # commit is what saves the transactions
        db.session.commit()
        assert db.session.query(Transactions).count() == transaction_count + 2
        transaction1 = Transactions.query.filter_by(type='CREDIT').first()
        assert transaction1.type == "CREDIT"
        # changing the title of the transaction
        transaction1.amount = "200"
        # saving the new title of the transaction
        db.session.commit()
        transaction2 = Transactions.query.filter_by(amount='2000').first()
        assert transaction2.type == "CREDIT"
        # checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == user_count
        assert db.session.query(Transactions).count() == transaction_count
