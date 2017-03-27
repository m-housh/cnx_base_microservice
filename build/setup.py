from setuptools import setup
import os

API_NAME = os.environ.get('API_NAME', 'api')
API_VERSION = os.environ.get('API_VERSION', '0.0.1')

setup(
    name=API_NAME,
    version=API_VERSION,
    description='HHE equipment api',
    author='Michael Housh',
    author_email='mhoush@houshhomeenergy.com',
    packages=['api'],
    package_dir={'api': 'api'},
    include_package_data=True,
    install_requires=[
        'connexion==1.1.5',
        'sqlalchemy==1.1.5',
        'psycopg2==2.7',
        'connexion_sql_utils==0.1.2',
        'gevent==1.2.1',
        'uwsgi==2.0.14',
    ],
    license="MIT license",
    zip_safe=False,
    keywords=API_NAME,
    test_suite='tests',
    tests_require=[]
)
