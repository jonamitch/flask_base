from flask_app import create_app, db
from flask_app.models import User, Post

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, use_debugger=False, use_reloader=True, passthrough_errors=True)
