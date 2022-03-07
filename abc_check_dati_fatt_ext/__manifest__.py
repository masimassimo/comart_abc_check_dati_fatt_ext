# -*- coding: utf-8 -*-
{
    'name': "abc_check_dati_fatt_ext",

    'summary': """
        Controllo campi obbligatori quando si genera una fattura da un ordine""",

    'description': """
        Controllo campi obbligatori quando si genera una fattura da un ordine
    """,

    'author': "ABC Strategie - Massimo Masi",
    'website': "https://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.5',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
