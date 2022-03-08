# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, ValidationError

class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"
    
    def _create_invoices(self, grouped=False, final=False, date=None):
        #Verifica Campi cliente
        
        for order in self:
            errorMessage =''
            if order.partner_id == False:
                errorMessage = errorMessage + 'Il campo Cliente è obbligatorio.'
            else:
                cliente = order.partner_id
                if cliente.vat == False and cliente.fiscalcode == False:
                    if (errorMessage != ''):
                        errorMessage = errorMessage + '\n'
                    errorMessage = errorMessage + 'I campi Partita IVA e Codice Fiscale del cliente sono vuoti. Compilare almeno un campo.'
                else:
                    if((not cliente.codice_destinatario or cliente.codice_destinatario == 'XXXXXXX' or cliente.codice_destinatario == '0000000') and not cliente.pec_destinatario):
                        if (errorMessage != ''):
                            errorMessage = errorMessage + '\n'
                        errorMessage = errorMessage + "Il Cliente " + cliente.name + " non ha impostato correttamente il Codice SDI o la PEC! Compilare uno di questi due campi in anagrafica per procedere."
                    cliente.check_vat()
                #TODO
                #se sono compilati va verificato il formato
                if cliente.street == False:
                    if (errorMessage != ''):
                            errorMessage = errorMessage + '\n'
                    errorMessage = errorMessage + 'Il campo Indirizzo del cliente non è compilato'
                if cliente.city == False:
                    if (errorMessage != ''):
                            errorMessage = errorMessage + '\n'
                    errorMessage = errorMessage + 'Il campo Città del cliente non è compilato'
                if cliente.zip == False:
                    if (errorMessage != ''):
                            errorMessage = errorMessage + '\n'
                    errorMessage = errorMessage + 'Il campo CAP del cliente non è compilato'
                if cliente.state_id == False:
                    if (errorMessage != ''):
                            errorMessage = errorMessage + '\n'
                    errorMessage = errorMessage + 'Il campo Provincia del cliente non è compilato'
                if cliente.codice_destinatario == False:
                    if (errorMessage != ''):
                            errorMessage = errorMessage + '\n'
                    errorMessage = errorMessage + 'Il campo Codice Destinatario del cliente non è compilato'
                if cliente.property_account_position_id == False:
                    if (errorMessage != ''):
                            errorMessage = errorMessage + '\n'
                    errorMessage = errorMessage + 'Il campo Posizione Fiscale del cliente non è compilato'
                if cliente.is_pa == True and cliente.ipa_code == False:
                    if (errorMessage != ''):
                            errorMessage = errorMessage + '\n'
                    errorMessage = errorMessage + 'Il campo Codice IPA del cliente non è compilato'
                if (errorMessage != ''):
                    raise UserError(errorMessage)
                
        return super()._create_invoices(grouped, final, date)

