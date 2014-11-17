import requests
import config


class MailGun():

    def __init__(self, auth):
        self.auth = auth

    def send_simple_message(self, data):
        return requests.post(
            "https://api.mailgun.net/v2/"+self.auth["domain"]+"/messages",
            auth=("api", self.auth["key"]),
            data={"from": self.auth["smtp"],
                  "to": data["receiver"],
                  "subject": data["subject"],
                  "text": data["content"]
            })

    def send_simple_html_message(self, data, files=None):
        attachments = []
        for attachment in files:
            attachments.append(('attachment', open(attachment)))
        return requests.post(
            "https://api.mailgun.net/v2/"+self.auth["domain"]+"/messages",
            auth=("api", self.auth["key"]),
            files=attachments,
            data={"from": self.auth["smtp"],
                  "to": data["receiver"],
                  "subject": data["subject"],
                  "html": data["content"],
            })


mailer = MailGun(config.MAILGUN_AUTH)