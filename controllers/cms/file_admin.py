from flask.ext.admin.contrib.fileadmin import FileAdmin
from flask.ext import login


class CustomFileAdmin(FileAdmin):
    def is_accessible(self):
        return login.current_user.is_authenticated()
