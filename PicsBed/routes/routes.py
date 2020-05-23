
# 视图函数文件

from flask import (
    Blueprint,
    views,
    render_template
)

bp = Blueprint('PicBed_bp', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


class LoginView(views.MethodView):

    def get(self, message=None):
        return render_template('login.html')

    def post(self):
        return 'login post'


class RegisterView(views.MethodView):

    def get(self, message=None):
        return render_template('register.html')

    def post(self):
        return 'register post'


class ResetPasswordView(views.MethodView):

    def get(self, message=None):
        return render_template('resetpwd.html')

    def post(self):
        return 'resetpwd post'


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/register/', view_func=RegisterView.as_view('register'))
bp.add_url_rule('/resetpwd/', view_func=ResetPasswordView.as_view('resetpwd'))
