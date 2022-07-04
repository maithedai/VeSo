# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2021-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    "name": "Odo Pharma Theme",
    "description": """""",
    "summary": "",
    "category": "Themes/Backend",
    "version": "15.0.1.0.1",
    'author': '',
    'company': '',
    'maintainer': '',
    'website': "",
    "depends": ['base', 'web', 'mail'],
    "data": [
        'security/ir.model.access.csv',
        'views/icons.xml',
        'views/layout.xml',
        'views/theme.xml',
        'views/assets.xml',
        'data/theme_data.xml',
    ],
    'assets': {
        'web.assets_backend': {
            '/odo_pharma_theme/static/src/scss/theme.scss',
            '/odo_pharma_theme/static/src/js/systray.js',
            '/odo_pharma_theme/static/src/js/load.js',
            '/odo_pharma_theme/static/src/js/chrome/sidebar_menu.js',
        },
        'web.assets_frontend': {
            '/odo_pharma_theme/static/src/scss/login.scss',
            '/odo_pharma_theme/static/src/scss/login.scss',
        },
        'web.assets_qweb': {
            '/odo_pharma_theme/static/src/xml/systray.xml',
            '/odo_pharma_theme/static/src/xml/top_bar.xml',
        },
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png',
    ],
    'license': 'LGPL-3',
    'pre_init_hook': 'test_pre_init_hook',
    'post_init_hook': 'test_post_init_hook',
    'installable': True,
    'application': False,
    'auto_install': False,
}
