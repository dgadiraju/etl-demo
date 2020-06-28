import os

DB_DETAILS = {
    'dev': {
        'RETAIL_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '139.99.209.131',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('RETAIL_DB_USER'),
            'DB_PASS': os.environ.get('RETAIL_DB_PASS')
        },
        'CUSTOMER_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '139.99.209.131',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('CUSTOMER_DB_USER'),
            'DB_PASS': os.environ.get('CUSTOMER_DB_PASS')
        }
    }
}