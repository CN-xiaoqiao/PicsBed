from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import config
    app.config.from_object(config)

    # 注册插件
    from utils import exts
    exts.init_app(app)

    import api
    api.init_app(app)
    return app


app = create_app()
