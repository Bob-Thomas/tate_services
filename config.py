import os.path as op
import platform

STATIC_FILES = op.join(op.dirname(__file__), 'static')
ARTIFACT_PATH = op.join(STATIC_FILES, 'artifacts')
QR_PATH = op.join(STATIC_FILES, 'barCodes')
PDF_PATH = op.join(STATIC_FILES, 'pdf')
LOG_PATH = op.join(STATIC_FILES, 'logs')
PERFORMANCE_PATH = op.join(STATIC_FILES, 'performances')
EXCEL_PATH = op.join(STATIC_FILES, 'excels')
MAILGUN_AUTH = {
    "key": "key-6lahuht78l8jrinjkai1gfdmbamgsxx2",
    "domain": "tate.bmthomas.nl",
    "smtp": "tate <postmaster@tate.bmthomas.nl>"
}
DIVIDER = '/'
if 'linux' != platform.system().lower():
    DIVIDER = '\\'
