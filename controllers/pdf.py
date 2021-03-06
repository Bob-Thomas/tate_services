from cStringIO import StringIO

from xhtml2pdf import pisa

import config


def create_pdf(pdf_data, file_name):
    path = config.PDF_PATH + "/" + file_name + ".pdf"
    pdf = open(path, 'wb')
    pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
    pdf.close()
    return path
