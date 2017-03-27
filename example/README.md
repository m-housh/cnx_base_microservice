Foo Example Api
===============

A small example of how to use the **mhoush/cnx_base_app** docker image.

Usage
-----

```bash
    $ docker pull mhoush/cnx_base_app:onbuild

    $ docker build -t base_app_example --build-arg APP_NAME=example \
        --build-arg APP_VERSION="0.1.10" .

    $ docker run -d --name some-postgres -e POSTGRES_PASSWORD=secret \
        postgres:alpine

    $ docker run -it --rm --link some-postgres:postgres \
        -e DB_HOST=postgres -e DB_PASSWORD=secret \
        -p 8080:8080 \
        base_app_example
```

Then navigate to http://localhost:8080/v1/ui to see the swagger file.
