# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCheckDatiFattExt(http.Controller):
#     @http.route('/abc_check_dati_fatt_ext/abc_check_dati_fatt_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_check_dati_fatt_ext/abc_check_dati_fatt_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_check_dati_fatt_ext.listing', {
#             'root': '/abc_check_dati_fatt_ext/abc_check_dati_fatt_ext',
#             'objects': http.request.env['abc_check_dati_fatt_ext.abc_check_dati_fatt_ext'].search([]),
#         })

#     @http.route('/abc_check_dati_fatt_ext/abc_check_dati_fatt_ext/objects/<model("abc_check_dati_fatt_ext.abc_check_dati_fatt_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_check_dati_fatt_ext.object', {
#             'object': obj
#         })
