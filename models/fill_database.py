# coding=utf-8
import random
from datetime import timedelta
from datetime import date
from random import randint

from database import db
from artifact import Artifact
from user import User
from user_groups import UserGroups
from insurer import Insurer
from insured_artifacts import InsuredArtifacts
from performance import Performance
from artifacts_in_performance import ArtifactsInPerformance
from cashier import Cashier
from cashier_login import CashierLogin
from page import Page


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
    'Duitsland',
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
# db.session.add(User(email='cashier@tate.com', password='test', first_name='verkoper', last_name='Dijkstra'))


db.session.add(Cashier(email='cashier@tate.com', first_name='Wouter', last_name='Dijkstra'))
db.session.add(CashierLogin(cashier=1, password="test"))

db.session.add(Cashier(email='cashier1@tate.com', first_name='Bob', last_name='Thomas'))
db.session.add(CashierLogin(cashier=2, password="test"))

db.session.add(Cashier(email='cashier2@tate.com', first_name='Nick', last_name='Bout'))
db.session.add(CashierLogin(cashier=3, password="test"))

db.session.add(UserGroups(group="Admin", user_id="1"))
db.session.add(UserGroups(group="PerformanceMaster", user_id="2"))
db.session.add(UserGroups(group="Manager", user_id="3"))
# db.session.add(UserGroups(group="Cashier", user_id="4"))

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
db.session.add(
    Artifact(name='HomoErectus', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found), image='homo-erectus.jpg', insured="PENDING", active=True))
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
db.session.add(
    Artifact(name='Neteldieren', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found), image='neteldieren.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='HomoHabilis', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found), image='homohablis.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Fosiel', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found),
             image='fosiel.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Tyranosaurus', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found), image='tyranosaurus.jpg', insured="NO", active=False))
db.session.add(
    Artifact(name='Roodborstje', reason=random.choice(reasons), geological_period=random.choice(time_periods),
             value=random.choice(prices), date_found=random_date(date(1900, 01, 01), date.today()),
             location_found=random.choice(location_found), image='roodborstje.jpg', insured="NO", active=False))
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
                           starting_date='2016-01-28', end_date='2016-05-01', image='roodborstje.jpg'))

db.session.add(ArtifactsInPerformance(artifact=1, performance=1))
db.session.add(ArtifactsInPerformance(artifact=2, performance=1))
db.session.add(ArtifactsInPerformance(artifact=3, performance=1))
db.session.add(ArtifactsInPerformance(artifact=4, performance=1))
db.session.add(ArtifactsInPerformance(artifact=5, performance=1))

db.session.add(Performance(name="Darwin tenoonstelling", information='tentoonstelling over het leven van darwin',
                           starting_date='2016-01-28', end_date='2016-05-01', image='slide1.jpg'))

db.session.add(ArtifactsInPerformance(artifact=6, performance=2))
db.session.add(ArtifactsInPerformance(artifact=7, performance=2))
db.session.add(ArtifactsInPerformance(artifact=8, performance=2))
db.session.add(ArtifactsInPerformance(artifact=9, performance=2))
db.session.add(ArtifactsInPerformance(artifact=10, performance=2))

db.session.add(Page(name='Leven van Darwin', title='Darwins leven',
                    content='Charles Robert Darwin (Shrewsbury (Shropshire), 12 februari 1809 – Downe (Kent), 19 april 1882) was een Engels autodidact op het gebied van natuurlijke historie, biologie en geologie. Darwin ontleent zijn roem aan zijn theorie dat evolutie van soorten wordt gedreven door natuurlijke selectie. Het bestaan van evolutie werd nog tijdens zijn leven binnen een groot deel van de wetenschappelijke gemeenschap geaccepteerd. De acceptatie van natuurlijke selectie als aandrijvend mechanisme liet langer op zich wachten en is tegenwoordig onomstreden.Darwin werd gelovig opgevoed en opgeleid volgens de filosofie van de in die tijd in Engeland gangbare natuurlijke theologie, die religie en wetenschap verenigde. Dankzij de waarnemingen en ontdekkingen die hij in de loop van zijn leven deed ging hij echter steeds meer twijfelen over zowel de gangbare ideeën over soortvorming als zijn persoonlijke geloof. Tijdens een onderzoeksreis met het schip de Beagle (1831-1836) bezocht Darwin Zuid-Amerika, Australië, het zuiden van Afrika en diverse eilandengroepen in de Grote en Indische Oceaan. Op al deze plekken bestudeerde hij de plaatselijke dieren, planten, fossielen en geologie. Een groot deel van zijn verdere leven was gewijd aan het onderzoeken en classificeren van de op zijn reis verzamelde voorwerpen en het was onder andere dankzij dit onderzoek dat hij op zijn theorie over het ontstaan van soorten kwam.Darwins werk zorgde voor een revolutie binnen de wetenschap, maar had ook invloed op maatschappij, filosofie en religie. De acceptatie van evolutie zette de mens neer als een diersoort, onderdeel van de natuur, in plaats van een boven de natuur staande levensvorm. Samen met de erfelijkheidsleer van Mendel vormt Darwins evolutietheorie tegenwoordig de basis van alle biologische kennis.',
                    image='slide1.jpg'))

db.session.add(Page(name='Intelligent Design', title='Intelligent Design',
                    content='Intelligent design (Engels, afgekort als ID, wordt vertaald als intelligent ontwerp) is de opvatting dat bepaalde kenmerken van het heelal en organismen het best worden verklaard als het werk van een intelligente "ontwerper". ID staat zodoende in contrast met de evolutietheorie, die erfelijkheid en selectiemechanismen (waaronder natuurlijke selectie) beschouwt als een afdoende verklaring voor het ontstaan van alle organismen. Hoewel er nog veel vragen open staan over het ontstaan van het leven en de erop volgende biologische evolutie, is er een overduidelijke consensus binnen de wetenschappelijke gemeenschap dat intelligent design geen wetenschap is, maar pseudowetenschap die gebruikmaakt van teleologische argumentatie.[1]De naam intelligent design wordt metonymisch gebruikt voor zowel de opvatting als voor de beweging die zich hard maakt voor het opnemen van bovenstaande opvatting in het curriculum van scholen in de Verenigde Staten. Ook in andere landen zijn ID-aanhangers.',
                    image='inteligent_design.jpg'))

db.session.add(Page(name='evolutie leer', title='evolutie leer - bomen en dieren',
                    content='Evolutie is het biologische begrip waarmee het proces van verandering in alle vormen van leven van generatie op generatie wordt aangegeven. Evolutiebiologie is het vakgebied dat de manier bestudeert waarop, en de oorzaken waardoor evolutie optreedt.Door middel van genen erft een organisme van zijn ouders kenmerken (die erfelijke eigenschappen worden genoemd). Veranderingen in genen (zogenaamde mutaties) zorgen ervoor dat nieuwe eigenschappen ontstaan in de nakomelingen van een organisme. Als een nieuwe eigenschap een organisme voordeel biedt zal dit organisme een grotere kans op overleven en nageslacht hebben. Dit mechanisme heet natuurlijke selectie en zorgt ervoor dat eigenschappen die voordeel bieden vaker voor gaan komen. Over veel generaties kan een populatie zoveel nieuwe eigenschappen ontwikkelen dat het een nieuwe soort wordt.De eerste bekende organismen waren bacteriën, Archaea en voorouders van de eukaryoten die ongeveer 3,5 miljard jaar geleden in waterig omgeving leefden. Uit de eukaryoten, waarvan het ontstaan verklaard wordt met de endosymbiosetheorie, ontstonden steeds ingewikkeldere eencellige en meercellige organismen. Het domein van de eukaryoten omvat 5 of 6 supergroepen. De bekende rijken schimmels en dieren worden samen gerekend als Opisthokonta tot de supergroep Unikonta. De planten vormen met algen als de groenwieren en de roodwieren de supergroep Archaeplastida. De in deze supergroep eenmaal verworven plastiden en bijbehorend erfelijk materiaal werden aan andere supergroepen doorgegeven door secundaire en tertiaire endosymbiose.Het eerste plantaardige leven één miljard jaar geleden op aarde bestond uit een bedekking met algen. De eerste herkenbare hogere planten dateren van 450 miljoen jaar geleden en de eerste fossielen van insecten zijn 400 miljoen jaar geleden ontstaan. De gewervelde dieren waren een grote groep van waterbewonende dieren, waarvan een groep van de kwastvinnigen geleidelijk het land heeft gekoloniseerd. De eerste viervoeters waren afhankelijk van water, vergelijkbaar met de tegenwoordige amfibieën, maar door de ontwikkeling van het amnion ongeveer 330 miljoen jaar geleden is een groep er in geslaagd de embryonale ontwikkeling in een ei buiten het water door te maken. Al snel splitsten de voorouders van zoogdieren (Synapsida) zich af. Uit de rest van de groepen (Sauropsida) zijn de tegenwoordig bekende reptielengroepen, als hagedissen en krokodillen, vele uitgestorven groepen als ichthyosauriërs, plesiosauriërs, pterosauriërs en de dinosauriërs met als enige overlevende groep de vogels ontstaan.',
                    image='evolutie_vis.jpg'))

db.session.add(Page(name='evolutie van de mens', title='evolutie - mens',
                    content='Evolutie is het biologische begrip waarmee het proces van verandering in alle vormen van leven van generatie op generatie wordt aangegeven. Evolutiebiologie is het vakgebied dat de manier bestudeert waarop, en de oorzaken waardoor evolutie optreedt.Door middel van genen erft een organisme van zijn ouders kenmerken (die erfelijke eigenschappen worden genoemd). Veranderingen in genen (zogenaamde mutaties) zorgen ervoor dat nieuwe eigenschappen ontstaan in de nakomelingen van een organisme. Als een nieuwe eigenschap een organisme voordeel biedt zal dit organisme een grotere kans op overleven en nageslacht hebben. Dit mechanisme heet natuurlijke selectie en zorgt ervoor dat eigenschappen die voordeel bieden vaker voor gaan komen. Over veel generaties kan een populatie zoveel nieuwe eigenschappen ontwikkelen dat het een nieuwe soort wordt.De eerste bekende organismen waren bacteriën, Archaea en voorouders van de eukaryoten die ongeveer 3,5 miljard jaar geleden in waterig omgeving leefden. Uit de eukaryoten, waarvan het ontstaan verklaard wordt met de endosymbiosetheorie, ontstonden steeds ingewikkeldere eencellige en meercellige organismen. Het domein van de eukaryoten omvat 5 of 6 supergroepen. De bekende rijken schimmels en dieren worden samen gerekend als Opisthokonta tot de supergroep Unikonta. De planten vormen met algen als de groenwieren en de roodwieren de supergroep Archaeplastida. De in deze supergroep eenmaal verworven plastiden en bijbehorend erfelijk materiaal werden aan andere supergroepen doorgegeven door secundaire en tertiaire endosymbiose.Het eerste plantaardige leven één miljard jaar geleden op aarde bestond uit een bedekking met algen. De eerste herkenbare hogere planten dateren van 450 miljoen jaar geleden en de eerste fossielen van insecten zijn 400 miljoen jaar geleden ontstaan. De gewervelde dieren waren een grote groep van waterbewonende dieren, waarvan een groep van de kwastvinnigen geleidelijk het land heeft gekoloniseerd. De eerste viervoeters waren afhankelijk van water, vergelijkbaar met de tegenwoordige amfibieën, maar door de ontwikkeling van het amnion ongeveer 330 miljoen jaar geleden is een groep er in geslaagd de embryonale ontwikkeling in een ei buiten het water door te maken. Al snel splitsten de voorouders van zoogdieren (Synapsida) zich af. Uit de rest van de groepen (Sauropsida) zijn de tegenwoordig bekende reptielengroepen, als hagedissen en krokodillen, vele uitgestorven groepen als ichthyosauriërs, plesiosauriërs, pterosauriërs en de dinosauriërs met als enige overlevende groep de vogels ontstaan.',
                    image='evolutie.jpg'))

db.session.add(Page(name='Geologische perioden', title='Geologische perioden',
                    content='Tijdperken worden ingedeeld in kleinere (sub-)tijdperken. De grootste tijdperken zijn de eonen, die worden opgedeeld in era&eacute;s. De geschiedenis van de Aarde wordt ingedeeld in drie officiële eonen: Archeïcum, Proterozoïcum en Fanerozoïcum. Het Fanerozoïcum wordt weer ingedeeld in drie era&eacute;s: Paleozoïcum, Mesozoïcum en Cenozoïcum. Op hun beurt worden era&eacute;s weer ingedeeld in periodes. Voorbeelden van periodes uit het Paleozoïcum zijn het Carboon en het Perm, het Mesozoïcum bestaat uit het Trias, het Jura en het Krijt en het Cenozoïcum uit het Paleogeen, het Neogeen en het Kwartair. Deze periodes worden weer ingedeeld in tijdvakken, die weer ingedeeld worden in tijdsnedes. Zo bestaat het Neogeen uit de tijdvakken Mioceen en Plioceen. Soms worden tijdsnedes weer ingedeeld in chrons, de kleinste eenheden in de geologische tijdschaal.Niet alle tijdperken met dezelfde status hebben een overeenkomstige lengte. Hoe ouder een tijdperk, hoe langer de duur. Dit komt doordat uit oudere tijdperken vaak minder details bekend zijn zodat het moeilijker wordt een duidelijker grens te maken. De periode Cryogenium (in het Proterozoïcum) duurt bijvoorbeeld meer dan 200 miljoen jaar, terwijl de jongste periode, het Kwartair, nog geen 3 miljoen jaar beslaat. De duur van de tijdperken is gebaseerd op de stratigrafie, de opeenvolging van wereldwijd gevonden gesteentelagen. Grenzen tussen tijdperken worden meestal gelegd bij afwisselingen of plotselinge overgangen in de stratigrafie. Voor de ouderdommen van gesteentelagen bestaat een eigen terminologie, die overeenkomt met de verschillende benamingen voor tijdperken. Zo is de periode Krijt genoemd naar het systeem Krijt; het systeem is de opeenvolging van lagen die in die periode zijn gevormd. In de tabel rechts is de relatie tussen stratigrafische eenheden en de corresponderende tijdperken verduidelijkt.Standaardisatie[bewerken]',
                    image='periode.jpg'))

db.session.commit()


