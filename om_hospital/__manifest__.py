{
    'name': 'Hospital Customizations',
    # 'version': '1.0',
    'category': 'Sales',
    'summary': 'Custom fields for Sales module',
    "author":"Mohtashim",
    "version":"17.0.1.3",
    "license":"LGPL-3",
    'depends': ['mail'],  # Make sure this module depends on the 'sale' module
    'data': [
        "security/ir.model.access.csv",
        "views/patient_readonly_views.xml",
        "views/appointment_views.xml",
        "views/menu.xml",
        "views/patient_views.xml"
    ],
    'installable': True,
    'application': False,
}
