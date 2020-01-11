from flask import Flask
from flask_admin import Admin, AdminIndexView
from flask_admin import expose
from flask_admin.base import MenuLink


class DashoboardView(AdminIndexView):
    @expose('/')
    def index(self):
        self.name = 'Dashboard'
        return self.render('admin/dashboard.html')


admin = Admin(template_mode='bootstrap3', index_view=DashoboardView(
    menu_icon_type='glyph',
    menu_icon_value='glyphicon-dashboard'))


admin.add_link(MenuLink(name='Back Home', url='/admin', category='Links'))
admin.add_link(MenuLink(name='Flask-Demos',
                        url='https://github.com/AngelLiang/Flask-Demos',
                        category='Links'))
admin.add_link(MenuLink(
    name='Baidu', url='http://www.baidu.com/', category='Links'))

app = Flask(__name__)
app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True
admin.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
