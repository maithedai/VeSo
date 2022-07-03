{
    'name': 'Lottery',
    'version': '14.0',
    "sequence": 1,
    'summary': 'Lottery',
    'complexity': "easy",
    'description': """
        Lottery
    """,
    'author': '',
    'depends': [
        'base', 'web', 'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/lot_customer_view.xml',
        'menus/lottery_menu.xml',
    ],
    'images': [

    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
