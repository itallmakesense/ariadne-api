from typing import Any

from ariadne import load_schema_from_path
from ariadne_graphql_modules import ObjectType, convert_case


class Person(ObjectType):
    __aliases__ = convert_case
    __schema__ = load_schema_from_path('types/person.graphql')

    @staticmethod
    def resolve_full_name(person: dict, *_: Any) -> str:
        return "%s %s" % (person["first_name"], person["last_name"])
