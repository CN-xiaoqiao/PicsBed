from .image import bp as image_bp

from flask import Flask


def init_app(app: Flask):
    app.register_blueprint(image_bp)
