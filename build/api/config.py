import os

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', 5432)
DB_USERNAME = os.environ.get('DB_USERNAME', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'postgres')
DB_NAME = os.environ.get('DB_NAME', 'postgres')

DB_URI = 'postgres+psycopg2://{user}:{password}@{host}:{port}/{db}'.format(
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    db=DB_NAME
)

SWAGGER_DIR = os.environ.get('SWAGGER_DIR', None)
SWAGGER_FILE_NAME = os.environ.get('SWAGGER_FILE_NAME', 'api.yml')

if SWAGGER_DIR is not None:
    SWAGGER_FILE = os.path.join(SWAGGER_DIR, SWAGGER_FILE_NAME)
else:
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    SWAGGER_FILE = os.path.join(
        os.path.dirname(THIS_DIR),
        'config',
        SWAGGER_FILE_NAME
    )

APP_PORT = int(os.environ.get('APP_PORT', 8080))

# Parse debug from the environment.
DEBUG = os.environ.get('DEBUG', False)
if str(DEBUG).lower() == 'true' or DEBUG == '1' or DEBUG is True:
    DEBUG = True
else:
    DEBUG = False
