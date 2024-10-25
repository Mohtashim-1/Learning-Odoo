{
    'name': 'Sales Customization',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Custom Fields for Product Template',
    'description': 'This module adds custom fields to the Product Template (Item Master).',
    'depends': ['base', 'product', 'sale_management'],  # Make sure the sale module is included
    'data': [
        'views/product_template_view.xml',
        'views/packaging_details.xml',
        'views/sale_order_line.xml',
        # 'views/sale_order.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
