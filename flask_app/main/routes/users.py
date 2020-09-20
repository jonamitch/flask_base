from flask import render_template
from flask_app.main import bp
from flask_login import login_required
from flask_app.models import User


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('main/user.html', user=user, posts=posts)
