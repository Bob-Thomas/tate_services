from flask import Flask, render_template
from models.database import db
from models.user import User
from controllers.cms.admin import admin
from flask.ext import login
from flask.ext import restful
from services.artifact_api import ArtifactApi
from services.ticket_api import TicketApi
from controllers.artifact import ArtifactController
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
    return render_template('ticket.html', order={
        'background': ArtifactController.get_base_64_artifact(ArtifactController.get_random_artifact().id),
        'barCode': "iVBORw0KGgoAAAANSUhEUgAAAcIAAAHCAQAAAABUY/ToAAADrElEQVR4nO2cS26kMBCGvxqQeglS DtBHMTeL5khzAzhKHyASXkZy65+FbRpIzyySyfRDVQuEwZ9sJKtcL2PiczL9+CQITjrppJNOOumk k/dHWpEWph7MrKU0zSx3GWLtNdx4tk7eF4kkiSBJmhsRlCDMADSS5tJFmhutOo+P9Z1Ofj8Zq36Z rIXpKBH0bmZHyYZYlZFZew+zdfKeyHbX1jSA8l3/hqahTYK07/do3+nk/yPtVVJWRsRD2dqm/lvH dPKxyQ/2EF1CUqIaQIliFLk95OTfyMnMzHognA6yIR5kA1DvGtnAObtlt5+tk3dFVqerCnSbS5hB Y5coqmoR10NOFsm2stG9tSL2iNgmAEQ0RASDg4zYQ/jVo9vN1sl7JKnaJwGdpJFq+4z5WSqqaqzh IreHnLxC5pUz5iBRI7Pju1365KhQmMGsb7QhPz+mk89CVr9shmoFpbKkpETWPiPlrcbO/TIn91Jt 5OLMEyQBNeuR7+am7mVuUzv5Qf7gly2mULaMtMqcuR5y8ioZa94+nMwIc7Psb9Uyygn9/uzxISd3 ctE+JQyUg9VaW0FSfRG0uGmP9Z1Ofh/JegejWS5kc7p0Wvaykcb3Mie3ssrH52w98QXoZiyIfAex TRZ+NcmCfC9z8iopnVogtthQDSD97EsfGwD9PKbc5R+N6eSzkGVJTAMG3btp6t+Wl+eWnPAgYbAk Qb44ppNPSeYIUDzU0NCpxQZKwiNn65cwpA23nq2Td0Wu40MlDNTUlP3KYSsWt8epnbwiNWxYYtKX VVKfwS7u6GvIya2s4kOLMsovxi6V0qFywqO69R4fcnIjdeWUkteVzgkz1VDarCvXQ05eJxsxHRMa Y6nzyAeEoPr2I+RK2X83ppNPQZY6xnCypXU2JmsEnFtBzZcFnTcHhB7rO538PpKLFXRxv3a1QjlL VpqeL3NyJ0s9NUBsE2E8G2EEwlwUj6b+DQMD4ovvZU7uZF8/tHj0UtU+lyrqy8X1kJNbcvXfj3y6 dW5k1tdTZUNXU2WTny9z8oNU7VNC1CvL6KKRLpYR4L69k9fJ5b8fAPZ6KhqpBIROVQXl5XPz2Tp5 z2T5T0zNa9jr3Ijp+G4lYu21H07u5cO/Y4g9TNaksnHFl2RhPkOYkQFYGL82ppPPRdY11AmIYGFM LXA26OZcOqTJmrx8cvN2s3XyHsmac82y1FPXtBhLeXWtB/F8mZM7KVHEpa160ba5vPWz0k466aST Tjrp5JORvwEDJC40gLedKgAAAABJRU5ErkJggg== ",
        'information': {
            'age': 19,
            'birthDate': "30-01-1995",
            'city': "Utrecht",
            'email': "smartcat007@hotmail.com",
            'firstName': "Bob",
            'lastName': "Thomas",
            'purchaseDate': "2014-11-17",
            'residence': "Woerden",
            'ticketId': 2,
            'zipCode': "3445AG"

        }
    })


init_login()
admin.init_app(app)
api.add_resource(TicketApi, '/ticket/<action>/<id>',
                 '/ticket/<action>/',
                 '/ticket/order')
api.add_resource(ArtifactApi, '/artifacts/<artifact_id>', '/artifacts/')

if __name__ == "__main__":
    app.debug = True
    app.static_folder = "files"
    app.run()