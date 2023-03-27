from app.db import init_db
from app.routes import home, dashboard, api
from app.utils import filters
from flask import Flask


def create_app(test_config=None):
    # setup app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        # in production use a key that is harder to guess
        SECRET_KEY='super_secret_key'
    )

    @app.route('/hello')
    def hello():
        return 'hello world'

    # register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(api)

    # register filters
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural

    # call db when flask app is ready
    init_db(app)

    return app
