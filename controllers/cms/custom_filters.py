from flask.ext.admin.babel import gettext
from flask.ext.admin.contrib.sqla.filters import BaseSQLAFilter
from flask.ext.admin.model.filters import BaseFilter

__author__ = 'bob'


class MyBaseFilter(BaseFilter):
    def __init__(self, column, name, options=None, data_type=None):
        super(MyBaseFilter, self).__init__(name, options, data_type)

        self.column = column


class MyBobFilter(BaseSQLAFilter):
    def apply(self, query, value):
        return query.filter(self.column == "Bob")

    def operation(self):
        return gettext('test')