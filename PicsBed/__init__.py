from flask import Flask

from PicBed.routes import bp as pb_bp


def create_app():
    app = Flask(__name__)

    import config
    app.config.from_object(config)

    from . import models
    models.init_app(app)

    app.register_blueprint(pb_bp)
    return app


app = create_app()
