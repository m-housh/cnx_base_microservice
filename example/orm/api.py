from functools import partial
from connexion_sql_utils import crud
from .foo import Foo


get_foo = partial(crud.get, Foo, limit=None)

post_foo = partial(crud.post, Foo, foo=None)
