from flask_app import create_app, db
from flask_app.models import User, Post
from secrets import initial_users

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        for user in initial_users:
            u = User(username=user['username'], email=user['email'], about_me=user['about_me'])
            u.set_password(user['password'])
            db.session.add(u)
            db.session.commit()

            p = Post(body='my first post!', author=u)
            db.session.add(p)
            p = Post(body='my second post!', author=u)
            db.session.add(p)
            p = Post(body='now im bored', author=u)
            db.session.add(p)

            db.session.commit()

    print('DB created successfully')
