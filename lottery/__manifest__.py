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
        'data/lot.tele.csv',
        'data/lot.tele.import.csv',
        'security/ir.model.access.csv',
        'views/lot_customer_view.xml',
        'views/return_stock_view.xml',
        'views/import_stock_view.xml',
        'menus/lottery_menu.xml',
    ],

    'assets': {
        'web.assets_qweb': [

        ],
        'web.assets_backend': [
            'lottery/static/src/scss/common.scss'
        ],
        'web.assets_tests': [
        ],
    },
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
