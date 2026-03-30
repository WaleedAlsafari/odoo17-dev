from ast import literal_eval

from odoo import http
from odoo.http import request
import io
import xlsxwriter



class PropertyXlsxReport(http.Controller):

    @http.route(route='/property/excel/report/<string:property_ids>', type='http', auth='user')
    def download_xlsx_report(self,property_ids):

        property_ids = request.env['estate.property'].browse(literal_eval(property_ids))
        print(property_ids)
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, options={'in_memory' : True})
        worksheet = workbook.add_worksheet(name='Properties')

        header_format = workbook.add_format({'bold' : True, 'bg_color' : '#D3D3D3', 'border' : 1, 'align' : 'center'})
        string_format = workbook.add_format({'border' : 1, 'align' : 'center'})
        price_format = workbook.add_format({'num_format' : '$##,##00.00','border' : 1, 'align' : 'center'})
        worksheet.set_column(0, 3, 20)

        headers = ['Name', 'Postcode', 'Bedrooms', 'Selling Price']

        for col, header in enumerate(headers):
            worksheet.write(0,col,header,header_format)

        row = 1
        for property in property_ids:
            worksheet.write(row,0,property.name,string_format)
            worksheet.write(row,1,property.postcode,string_format)
            worksheet.write(row,2,property.bedrooms,string_format)
            worksheet.write(row,3,property.selling_price,price_format)
            row += 1
        

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