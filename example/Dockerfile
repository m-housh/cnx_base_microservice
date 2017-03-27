FROM mhoush/cnx_base_app:onbuild

# uwsgi socket name that is written to /var/run/<API_SOCKET_NAME>.sock
# good if using an application gateway, that can connect to a unix socket.
# (which is the behavior of the default ``uwsgi.yml``)
ENV API_SOCKET_NAME=equipment

# debug mode ``true``, ``false``, ``0`` = false, ``1`` = true
# sets debug in the app and for logging.
ENV DEBUG=true

# Add your swagger yaml file to the /app/config/api.yml path
#COPY api.yml /app/config/api.yml

# You can also override the default uwsgi.yml file.
#COPY uwsgi.yml /app/config/uwsgi.yml

# Add your orm package dir to /app/api/orm.
# The orm should be a python package with that holds your database
# models.  The should inherit from ``DbModel`` in api.db module.
# This is also where you should declare your api methods that are called
# from the swagger yaml file.
#COPY orm /app/api/orm

# Install the package with your orm inside.
# The install script allows you to set a custom name and version
# for the api.
# If you want the default `api` and version `0.0.1` then you can
# do...
# RUN pip install /app
#RUN /bin/sh /install.sh --name equipment_api --version "0.3.3" && \
#    rm -rf /install.sh

#CMD ["/usr/local/bin/uwsgi", "--yaml", "config/uwsgi.yml"]
