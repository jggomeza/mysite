import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

# Run app
# flask --app flaskr --debug run
# flask --app flaskr --debug run --host=0.0.0.0
# flask --app flaskr --debug run --host=0.0.0.0 --port=8080
# flask --app flaskr init-db

# Install the Project
# pip install -e .

# Test Coverage
# pip install pytest coverage
# pytest
# coverage run -m pytest
# coverage report
# coverage html

# Deploy to Production
# pip install wheel
# python setup.py bdist_wheel
# pip install flaskr-1.0.0-py3-none-any.whl
# flask --app flaskr init-db

# Configure the Secret Key
# python -c "import secrets; print(secrets.token_hex())"

# Run with a Production Server
# pip install waitress
# waitress-serve --call 'flaskr:create_app'