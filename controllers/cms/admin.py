import config
from flask.ext.admin import Admin
from flask.ext.admin.contrib.fileadmin import FileAdmin
from controllers.cms.adminIndex import CustomAdminIndexView
from controllers.cms.file_admin import CustomFileAdmin
from models.database import db

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

admin.add_view(UserView(User, db.session))
admin.add_view(UserGroupsView(UserGroups, db.session))
admin.add_view(ArtifactView(Artifact, db.session))
admin.add_view(InsurerView(Insurer, db.session))
admin.add_view(InsuredArtifactsView(InsuredArtifacts, db.session))
admin.add_view(CustomFileAdmin(config.STATIC_FILES, '/static/', name='Static Files'))
