from database import db
from artifact import Artifact
from user import User
from user_groups import UserGroups
from insurer import Insurer
from insured_artifacts import InsuredArtifacts
from performance import Performance
from artifacts_in_performance import ArtifactsInPerformance
from ticket import Ticket
from quotation import Quotation
from request import Request
from agreement import Agreement
import random
from datetime import timedelta
from datetime import date
from random import randint


def random_date(start, end):
    return start + timedelta(
        seconds=randint(0, int((end - start).total_seconds())))


time_periods = ['neogeen', 'paleogeen', 'krijt', 'trias', 'mioceen', 'plioceen', 'carboon', 'perm', 'fanerozoicum']

reasons = [
    'Zag er mooi uit',
    'er zijn nog veel mysterisch over dit tijd perk',
    'het is een pracht stuk en past mooi in de catelogus',
    'redenen'
]

prices = [100.00,
          200.00,
          999.00,
          2000.00,
          213131.00
]

location_found = [
    'Duitsland'
    'Frankrijk',
    'Nederland',
    'Oosterijk',
    'China',
    'Japan',
    'Madagascar'
]

db.drop_all()
db.create_all()

db.session.add(User(email='smartcat007@hotmail.com', password='test', first_name='Bob', last_name='Thomas'))
db.session.add(User(email='performance@tate.com', password='test', first_name='Bob', last_name='Thomas'))
db.session.add(User(email='manager@tate.com', password='test', first_name='Wouter', last_name='Dijkstra'))

db.session.add(UserGroups(group="Admin", user_id="1"))
db.session.add(UserGroups(group="PerformanceMaster", user_id="2"))

db.session.add(Insurer(name="Bob", email="smartcat007@hotmail.com", company="Bobisoft"))
db.session.add(Insurer(name="Nick", email="smartcat007@hotmail.com", company="nickisoft"))
db.session.add(Insurer(name="Jim", email="smartcat007@hotmail.com", company="jimmysoft"))

db.session.add(
    Artifact(name='Leeuw', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='leeuw.jpg', insured="YES", active=True))
db.session.add(
    Artifact(name='Hond', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='hond.jpg', insured="YES", active=True))
db.session.add(
    Artifact(name='Baksteen', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='baksteen.jpg', insured="YES", active=True))
db.session.add(Artifact(name='HomoErectus', reason="Zag er prachtig uit in goede staat", geological_period="Krijt",
                        value='2900.30', image='homo-erectus.jpg', insured="PENDING", active=True))
db.session.add(
    Artifact(name='Kiwi', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='kiwi.jpg', insured="PENDING", active=True))
db.session.add(
    Artifact(name='Kea', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='kea.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Haai', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='haai.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Palm Boom', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='palmboom.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='HomoSapien', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='homosapien.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Giraf', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='giraf.jpg', insured="NO", active=False))
db.session.add(Artifact(name='Neteldieren', reason="Zag er prachtig uit in goede staat", geological_period="Krijt",
                        value='2900.30', image='neteldieren.jpg', insured="NO", active=False))
db.session.add(Artifact(name='HomoHabilis', reason="Zag er prachtig uit in goede staat", geological_period="Krijt",
                        value='2900.30', image='homohablis.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Fosiel', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='fosiel.jpg', insured="NO", active=False))
db.session.add(Artifact(name='Tyranosaurus', reason="Zag er prachtig uit in goede staat", geological_period="Krijt",
                        value='2900.30', image='tyranosaurus.jpg', insured="NO", active=False))
db.session.add(Artifact(name='Roodborstje', reason="Zag er prachtig uit in goede staat", geological_period="Krijt",
                        value='2900.30', image='roodborstje.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Krokodil', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='krokodil.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Zebra', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='zebra.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Kraai', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='kraai.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Slang', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='slang.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Zwijn', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='zwijn.jpg', insured="NO", active=False))

db.session.add(InsuredArtifacts(insurer=1, artifact=1, request_date='1970-01-01', end_date='2014-01-01'))
db.session.add(InsuredArtifacts(insurer=2, artifact=2, request_date='1970-01-01', end_date='2014-01-01'))
db.session.add(InsuredArtifacts(insurer=3, artifact=3, request_date='1970-01-01', end_date='2014-01-01'))
db.session.add(InsuredArtifacts(insurer=1, artifact=4, request_date='1970-01-01', end_date='2014-01-01'))
db.session.add(InsuredArtifacts(insurer=1, artifact=5, request_date='1970-01-01', end_date='2014-01-01'))

db.session.add(Performance(name="Vogel tentoonstelling", information='tentoonstelling over de evolutie van vogels',
                           starting_date='2016-01-28', end_date='2016-05-01'))

db.session.add(ArtifactsInPerformance(artifact=1, performance=1))
db.session.add(ArtifactsInPerformance(artifact=2, performance=1))
db.session.add(ArtifactsInPerformance(artifact=3, performance=1))
db.session.add(ArtifactsInPerformance(artifact=4, performance=1))
db.session.add(ArtifactsInPerformance(artifact=5, performance=1))

db.session.commit()


