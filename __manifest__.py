{
    'name': "Acquisti Peso Totale ",

    'summary': "Modulo sviluppato con lo scopo di calcolare il peso totale dei prodotti sul modulo acquisti",

    'description': """
Long description of module's purpose
    """,

    'author': "",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Acquisti prodotti',
    'version': '19.0.1.0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase', 'purchase_stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}

