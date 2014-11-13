from database import db
from artifact import Artifact
from user import User
from user_groups import UserGroups
from ticket import Ticket
from insurer import Insurer
from insured_artifacts import InsuredArtifacts
from performance import Performance
from agreement import Agreement
from quotation import Quotation
from request import Request
from room import Room


db.drop_all()
db.create_all()


db.session.add(User(email='smartcat007@hotmail.com', password='test', first_name='Bob', last_name='Thomas'))
db.session.commit()


