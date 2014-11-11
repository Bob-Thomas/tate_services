from flask import Flask
from models.database import db
from models.user import User
from controllers.cms.admin import admin
from flask.ext import login


app = Flask(__name__)
app.secret_key = 'changethis'


def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

init_login()
admin.init_app(app)


if __name__ == "__main__":
    app.debug = True
    app.static_folder = "files"
    app.run()