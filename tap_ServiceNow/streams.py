"""Stream type classes for tap-servicenow."""

from __future__ import annotations

import typing as t
from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_servicenow.client import ServiceNowStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class InteractionStream(ServiceNowStream):
    """Define custom stream."""

    name = "interaction"
    path = "/api/now/table/interaction?&type=chat"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property("number", th.StringType),
        th.Property(
            "sys_class_name",
            th.StringType,
            description="Type of class",
        ),
        th.Property(
            "sys_id",
            th.StringType,
            description="The ID of the record in the system.",
        ),
    ).to_dict()


# class GroupsStream(ServiceNowStream):
#     """Define custom stream."""

#     name = "groups"
#     path = "/groups"
#     primary_keys: t.ClassVar[list[str]] = ["id"]
#     replication_key = "modified"
#     schema = th.PropertiesList(
#         th.Property("name", th.StringType),
#         th.Property("id", th.StringType),
#         th.Property("modified", th.DateTimeType),
#     ).to_dict()
