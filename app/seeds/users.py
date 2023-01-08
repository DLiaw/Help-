from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        first_name='Demoo',last_name='Lee', email='demo@gmail.com', password='password')
    user1 = User(
        first_name='Nhut',last_name='Lee', email='Nhut@gmail.com', password='password')
    user2 = User(
        first_name='Curtis',last_name='Lee', email='Curtis@gmail.com', password='password')
    user3 = User(
        first_name='Dylan',last_name='Lee', email='Dylan@gmail.com', password='password')
    user4 = User(
        first_name='Jarod',last_name='Lee', email='Jarod@gmail.com', password='password')
    user5 = User(
        first_name='Sam',last_name='Lee', email='sam@gmail.com', password='password')
    user6 = User(
        first_name='LingLing',last_name='Lee', email='Lingling@gmail.com', password='password')

    db.session.add(demo)
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
