#!/usr/bin/env python

import logging
from . import db, utils, config
import connexion

# Setup logging based on ``DEBUG``
if config.DEBUG is True:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logging.info('DEBUG: {}'.format(config.DEBUG))

# Create the application.
app = connexion.App(__name__, debug=config.DEBUG, server='gevent',
                    port=config.APP_PORT)
# registry the swagger file
app.add_api(config.SWAGGER_FILE)

application = app.app
utils.create_all()


@application.teardown_appcontext
def shutdown_db_session(exception=None):
    db.Session.remove()
