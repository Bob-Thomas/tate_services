from flask import Flask, render_template
from models.database import db
from models.user import User
from controllers.cms.admin import admin
from flask.ext import login
from flask.ext import restful
from services.artifact_api import ArtifactApi
from services.ticket_api import TicketApi

app = Flask(__name__)
app.secret_key = 'changethis'
api = restful.Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

@app.route('/test')
def test():
    return render_template('ticket.html')

init_login()
admin.init_app(app)
api.add_resource(TicketApi, '/ticket/<action>/<id>',
                            '/ticket/<action>/',
                            '/ticket/order')
api.add_resource(ArtifactApi, '/artifact/<action>/<id>')

if __name__ == "__main__":
    app.debug = True
    app.static_folder = "files"
    app.run()