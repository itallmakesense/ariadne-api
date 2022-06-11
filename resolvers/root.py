from typing import Any

from ariadne import load_schema_from_path
from ariadne_graphql_modules import DeferredType, ObjectType, convert_case


class Query(ObjectType):
    __aliases__ = convert_case
    __requires__ = [DeferredType('Person')]
    __schema__ = load_schema_from_path('types/root.graphql')

    @staticmethod
    def resolve_people(*_: Any) -> list[dict[str, Any]]:
        return [
            {'first_name': 'John', 'last_name': 'Doe', 'age': 21},
            {'first_name': 'Bob', 'last_name': 'Boberson', 'age': 24},
        ]
