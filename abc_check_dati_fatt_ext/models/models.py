# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError

#class SaleAdvancePaymentInv(models.TransientModel):
#    _name = "sale.advance.payment.inv"
#    _inherit = "sale.advance.payment.inv"

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"
    
    def _create_invoices(self, grouped=False, final=False, date=None):
        #Verifica Campi cliente
        
        #sale_order = self.env['sale.order'].browse(self._context.get('active_id'))

        for order in self:
            if order.partner_id == False:
                raise UserError('Il campo Cliente è obbligatorio.')
            else:
                cliente = order.partner_id
                if cliente.vat == False and cliente.fiscalcode == False:
                    raise UserError('I campi partita iva e codice fiscale del cliente sono vuoti. Compilare almeno un campo.')
                else:
                    cliente.check_vat()
                #TODO
                #se sono compilati va verificato il formato
                if cliente.street == False:
                    raise UserError('Il campo indirizzo del cliente non è compilato')
                if cliente.city == False:
                    raise UserError('Il campo città del cliente non è compilato')
                if cliente.zip == False:
                    raise UserError('Il campo CAP del cliente non è compilato')
                if cliente.state_id == False:
                    raise UserError('Il campo Provincia del cliente non è compilato')
                if cliente.codice_destinatario == False:
                    raise UserError('Il campo Provincia del cliente non è compilato')
                if cliente.property_account_position_id == False:
                    raise UserError('Il campo Posizione Fiscale del cliente non è compilato')
                if cliente.is_pa == True and cliente.ipa_code == False:
                   raise UserError('Il campo Codice IPA del cliente non è compilato')
        super()._create_invoices(grouped, final, date)

# class abc_check_dati_fatt_ext(models.Model):
#     _name = 'abc_check_dati_fatt_ext.abc_check_dati_fatt_ext'
#     _description = 'abc_check_dati_fatt_ext.abc_check_dati_fatt_ext'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
