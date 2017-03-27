cnx_base_app
============

A docker image that allows to quickly create a microservice with the boiler-plate
builtin.

Just create an *api.yml* file to use for the swagger definition and a python
package to mount to ``/app/api/orm`` that includes the database model(s) and
api methods defined in the *api.yml* file. 

Packages Included
-----------------

**Base Image:** python:alpine (3.6.0)  

**Python Packages**:  
- connexion==1.1.5  
- sqlalchemy==1.1.5
- psycopg2==2.7
- connexion_sql_utils==0.1.2
- gevent==1.2.1
- uwsgi==2.0.14  

**Additional Packages**: make  

Usage
-----

See the example app for how to setup the package.

There are two flavors of images, onbuild is typically the easiest, but requires
certain naming conventions in your package dir. The swagger file should be
in the base directory (where you have your Dockerfile) using the name
*api.yml* , which will be copied to ``/app/config/api.yml`` onbuild and 
you should have a python package named *orm* which will be copied to
``/app/api/orm`` onbuild.  The onbuild also accepts some ``--build-args``.

If you are not using the onbuild variant then, you should copy your swagger file
to ``/app/config/api.yml`` as well as your package to ``/app/api/orm``.  You can
then include the **APP_PORT** as an environment variable in your Dockerfile.
You should also call the ``/app/install.sh`` with an optional ``--name`` 
(same as **APP_NAME**) and an optional ``--version`` (same as **APP_VERSION**)
to call the python setup.py properly.

**NOTE:**  You can call the ``/app/install.sh`` without any options to use the
default values shown in the onbuild-args section.  Or just call 
``pip install /app`` in your Dockerfile.

On either image to override the default *uwsgi.yml* you can copy a yaml
configuration file to ``/app/config/uwsgi.yml``.  The default *uwsgi.yml* listens
on a TCP socket the envrionment variable **APP_PORT**. Which is best if used
behind an *api-gateway* such as *nginx*.  However for testing it can often
be nice to listen for *http* requests, which is when you should add your own
*uwsgi.yml* file.

ONBUILD-Args
------------

The following options can be used when building your dockerfile with the
``--build-arg APP_NAME=example`` syntax.  

- **APP_NAME:**  A custom name for the python setup.py script (defaults to api)
- **APP_VERSION:**  A custom version for the python setup.py script (defaults to 0.0.1)
- **APP_PORT:**  A custom port to use for the uwsgi socket. (defaults to 8080)

License
-------

MIT license
