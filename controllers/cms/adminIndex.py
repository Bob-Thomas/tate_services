from flask import url_for, request
from flask.ext.admin import helpers, expose
from werkzeug.utils import redirect
from flask.ext import login
from flask.ext import admin

from controllers.loginLogger import LoginLogger
from login_form import LoginForm


class CustomAdminIndexView(admin.AdminIndexView):
    logger = LoginLogger()

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(CustomAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            self.logger.write_to_log(form.get_user()['data'].email)
            user = form.get_user()
            login.login_user(user['data'])
        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(CustomAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))