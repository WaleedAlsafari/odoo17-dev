from odoo import http
from odoo.http import request
import io
import xlsxwriter



class PropertyXlsxReport(http.Controller):

    @http.route(route='/property/excel/report', type='http', auth='user')
    def download_xlsx_report(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, options={'in_memory' : True})
        worksheet = workbook.add_worksheet(name='Properties')

        header_format = workbook.add_format({'bold' : True, 'bg_color' : '#D3D3D3', 'border' : 1, 'align' : 'center'})

        headers = ['Name', 'Postcode', 'Bedrooms', 'Selling Price']