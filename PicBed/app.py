from flask import Flask
from PicBed.routes import bp as pb_bp


def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(pb_bp)
    return flask_app


app = create_app()


if __name__ == '__main__':
    app.run()


