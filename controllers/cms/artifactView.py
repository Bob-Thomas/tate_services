import os.path as op

from flask import url_for
from markupsafe import Markup
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import form
from werkzeug.utils import secure_filename
from flask.ext import login

import config


def prefix_name(obj, file_data):
    parts = op.splitext(file_data.filename)
    return secure_filename('file-%s%s' % parts)


class ArtifactView(ModelView):
    edit_template = "create.html"

    def is_accessible(self):
        return login.current_user.is_authenticated()

    def list_thumbnail(view, context, model, name):
        if not model.image:
            return ''
        return Markup('<img src="%s">' % url_for('static',
                                                 filename='artifacts/' + form.thumbgen_filename(model.image)))

    column_list = ('name', 'geological_period', 'insured', 'active', 'value', 'image')

    column_formatters = {
        'image': list_thumbnail
    }
    form_extra_fields = {
        'image': form.ImageUploadField('Image',
                                       base_path=config.ARTIFACT_PATH,
                                       thumbnail_size=(100, 100, True))
    }
    form_widget_args = {
        'insured': {
            'disabled': True
        },
        'active': {
            'disabled': True
        }
    }