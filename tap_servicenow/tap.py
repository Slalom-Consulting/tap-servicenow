"""ServiceNow tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_servicenow import streams


class TapServiceNow(Tap):
    """ServiceNow tap class."""

    name = "tap-servicenow"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "username",
            th.StringType,
            required=True,
            secret=False,
            description="The Username of the ServiceNow service account",
        ),
        th.Property(
            "password",
            th.StringType,
            required=True,
            secret=True,
            description="The Password of the ServiceNow service account",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType,
            description="The url for the API service",
        )
    ).to_dict()

    def discover_streams(self) -> list[streams.ServiceNowStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.IncidentStream(self),
            streams.InteractionStream(self),
            streams.KbUseStream(self),
            streams.ScReqItemStream(self),
            streams.SCRequest(self),
            streams.SCTaskStream(self),
            streams.SpLogStream(self),
            streams.SysDbObjectStream(self),
            streams.SysDictionaryStream(self),
            streams.SysUserGroup(self),
            streams.SysUserStream(self),
        ]


if __name__ == "__main__":
    TapServiceNow.cli()
