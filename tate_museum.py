from flask import Flask
from controllers.admin import admin
import models
from models import *

app = Flask(__name__)
app.secret_key = 'changethis'

admin.init_app(app)

if __name__ == "__main__":
    app.debug = True
    app.run()