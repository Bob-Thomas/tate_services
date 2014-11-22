from datetime import datetime
from flask import url_for, request
from flask.ext.admin import helpers, expose
from werkzeug.utils import redirect
from flask.ext import login
from flask.ext import admin
import config
from login_form import LoginForm


class CustomAdminIndexView(admin.AdminIndexView):
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
            log = open(config.LOG_PATH+config.DIVIDER+'login_log.txt', 'a')
            log.write("user {} logged in at {}\n".format(form.get_user().email, str(datetime.now())))
            log.close()
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(CustomAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))