from flask.ext.admin import Admin

import config
from controllers.cms.adminIndex import CustomAdminIndexView
from controllers.cms.aritfacts_performance_view import ArtifactsInPerformanceView
from controllers.cms.file_admin import CustomFileAdmin
from controllers.cms.performance_view import PerformanceView
from models.artifacts_in_performance import ArtifactsInPerformance
from models.database import db
from models.performance import Performance
from models.ticket import Ticket
from ticket_view import TicketView
from user_view import UserView
from models.user import User
from user_group_view import UserGroupsView
from models.user_groups import UserGroups
from artifactView import ArtifactView
from models.artifact import Artifact
from insurer_view import InsurerView
from models.insurer import Insurer
from insured_artifacts_view import InsuredArtifactsView
from models.insured_artifacts import InsuredArtifacts


admin = Admin(name='Tate admin panel', index_view=CustomAdminIndexView(), base_template='my_master.html')

admin.add_view(UserView(User, db.session, category='User'))
admin.add_view(UserGroupsView(UserGroups, db.session, category='User'))
admin.add_view(TicketView(Ticket, db.session))
admin.add_view(ArtifactView(Artifact, db.session, category='Artifacts'))
admin.add_view(InsurerView(Insurer, db.session))
admin.add_view(InsuredArtifactsView(InsuredArtifacts, db.session, category='Artifacts'))
admin.add_view(PerformanceView(Performance, db.session, category='Performance'))
admin.add_view(ArtifactsInPerformanceView(ArtifactsInPerformance, db.session, category='Performance'))
admin.add_view(CustomFileAdmin(config.STATIC_FILES, '/static/', name='Static Files'))
