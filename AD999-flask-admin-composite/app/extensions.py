from flask import request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babelex import Babel
from flask_admin import Admin

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'
# login_manager.login_message = '请先登录'


from app.admin.admin_index import AdminIndexView  # noqa
admin = Admin(template_mode='bootstrap3', index_view=AdminIndexView(
    menu_icon_type='glyph', menu_icon_value='glyphicon-home'
))

babel = Babel()


@babel.localeselector
def get_locale():
    override = request.args.get('lang')

    if override:
        session['lang'] = override

    return session.get('lang', 'zh_CN')


def register_extensions(app):
    db.init_app(app)
    db.app = app
    babel.init_app(app)
    admin.init_app(app)
    admin.name = app.config['APP_NAME']
    from app.admin.modelviews import register_model_views
    register_model_views(admin, app)
    login_manager.init_app(app)
