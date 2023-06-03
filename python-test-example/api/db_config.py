# -*- coding: utf-8 -*
import os

# MySQL Settings
db_config = {
    'db_type': 'mysql+pymysql',
    'username': os.getenv('MYSQL_USER', 'test_user'),
    'password': os.getenv('MYSQL_PASSWORD', 'test_password'),
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'port': '3306',
    'db_name': 'sample'
}
