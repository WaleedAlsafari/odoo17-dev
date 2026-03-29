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

        for col, header in enumerate(headers):
            worksheet.write(0,col,header,header_format)

        workbook.close()
        output.seek(0)

        file_name = 'Property Report.xlsx'

        return request.make_response(
            output.getvalue(),
            headers= [
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', f'attachment; filename={file_name}')
            ]
        )