{
    'name': 'CRM Social Profile',
    'version': '15.0.1.0.0',
    'summary': 'Redes sociales en contactos + perfil completo + website de clientes con búsqueda',
    'author': 'LTG',
    'license': 'LGPL-3',
    'depends': ['base', 'account', 'crm', 'website'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_view_inherit.xml',
        'views/website_menu.xml',
    ],
    'test': [
        'tests/__init__.py',
    ],

    'installable': True,
    'application': False,
}
