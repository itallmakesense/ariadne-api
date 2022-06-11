from ariadne.asgi import GraphQL
from ariadne_graphql_modules import make_executable_schema

from resolvers import TYPE_RES


schema = make_executable_schema(*TYPE_RES)
app = GraphQL(schema, debug=True)
