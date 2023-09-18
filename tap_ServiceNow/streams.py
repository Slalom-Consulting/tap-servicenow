"""Stream type classes for tap-servicenow."""

from __future__ import annotations

import typing as t
from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_servicenow.client import ServiceNowStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class IncidentStream(ServiceNowStream):
    """Define Incident stream."""

    name = "incident"
    path = "/api/now/table/incident?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("active", th.BooleanType),
        th.Property("activity_due", th.StringType),
        th.Property("additional_assignee_list", th.StringType),
        th.Property("approval_history", th.StringType),
        th.Property("approval_set", th.StringType),
        th.Property("approval", th.StringType),
        th.Property("assigned_to", th.StringType),
        th.Property("assignment_group", th.StringType),
        th.Property("business_duration", th.StringType),
        th.Property("business_impact", th.StringType),
        th.Property("business_service", th.StringType),
        th.Property("business_stc", th.StringType),
        th.Property("calendar_duration", th.StringType),
        th.Property("calendar_stc", th.StringType),
        th.Property("caller_id", th.StringType),
        th.Property("category", th.StringType),
        th.Property("cause", th.StringType),
        th.Property("caused_by", th.StringType),
        th.Property("child_incidents", th.StringType),
        th.Property("close_code", th.StringType),
        th.Property("close_notes", th.StringType),
        th.Property("closed_at", th.DateTimeType),
        th.Property("closed_by", th.StringType),
        th.Property("cmdb_ci", th.StringType),
        th.Property("comments_and_work_notes", th.StringType),
        th.Property("comments", th.StringType),
        th.Property("company", th.StringType),
        th.Property("contact_type", th.StringType),
        th.Property("contract", th.StringType),
        th.Property("correlation_display", th.StringType),
        th.Property("correlation_id", th.StringType),
        th.Property("description", th.StringType),
        th.Property("due_date", th.StringType),
        th.Property("escalation", th.StringType),
        th.Property("expected_start", th.StringType),
        th.Property("follow_up", th.StringType),
        th.Property("group_list", th.StringType),
        th.Property("impact", th.StringType),
        th.Property("incident_state", th.StringType),
        th.Property("knowledge", th.BooleanType),
        th.Property("location", th.StringType),
        th.Property("made_sla", th.BooleanType),
        th.Property("notify", th.StringType),
        th.Property("number", th.StringType),
        th.Property("opened_at", th.DateTimeType),
        th.Property("opened_by", th.StringType),
        th.Property("order", th.StringType),
        th.Property("origin_id", th.StringType),
        th.Property("origin_table", th.StringType),
        th.Property("parent_incident", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("priority", th.StringType),
        th.Property("problem_id", th.StringType),
        th.Property("reassignment_count", th.StringType),
        th.Property("reopen_count", th.StringType),
        th.Property("reopened_by", th.StringType),
        th.Property("reopened_time", th.StringType),
        th.Property("resolved_at", th.DateTimeType),
        th.Property("resolved_by", th.StringType),
        th.Property("rfc", th.StringType),
        th.Property("route_reason", th.StringType),
        th.Property("service_offering", th.StringType),
        th.Property("severity", th.StringType),
        th.Property("short_description", th.StringType),
        th.Property("skills", th.StringType),
        th.Property("sla_due", th.StringType),
        th.Property("sn_esign_document", th.StringType),
        th.Property("sn_esign_esignature_configuration", th.StringType),
        th.Property("state", th.StringType),
        th.Property("subcategory", th.StringType),
        th.Property("sys_class_name", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_domain_path", th.StringType),
        th.Property("sys_domain", th.StringType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("task_effective_number", th.StringType),
        th.Property("time_worked", th.StringType),
        th.Property("u_choice_5", th.StringType),
        th.Property("u_computer", th.StringType),
        th.Property("u_converted_to", th.StringType),
        th.Property("u_dell_service_number", th.StringType),
        th.Property("u_dell_service_tag", th.StringType),
        th.Property("u_device_exception", th.StringType),
        th.Property("u_due_date", th.StringType),
        th.Property("u_failure_type", th.StringType),
        th.Property("u_feature", th.StringType),
        th.Property("u_follow_up", th.StringType),
        th.Property("u_high_security", th.BooleanType),
        th.Property("u_ibm_ticket_last_modified", th.StringType),
        th.Property("u_ibm_ticket_number", th.StringType),
        th.Property("u_incorrectly_converted", th.BooleanType),
        th.Property("u_initiated_from", th.StringType),
        th.Property("u_initiating_interaction", th.StringType),
        th.Property("u_integer_1", th.StringType),
        th.Property("u_journal_1", th.StringType),
        th.Property("u_keep_open", th.BooleanType),
        th.Property("u_message_id", th.StringType),
        th.Property("u_offense_id", th.StringType),
        th.Property("u_received_device_model", th.StringType),
        th.Property("u_received_email", th.StringType),
        th.Property("u_responded_to", th.BooleanType),
        th.Property("u_string_1", th.StringType),
        th.Property("u_string_2", th.StringType),
        th.Property("u_string_3", th.StringType),
        th.Property("u_tier_1", th.BooleanType),
        th.Property("u_tier_2", th.BooleanType),
        th.Property("u_tier_3", th.BooleanType),
        th.Property("u_topic", th.StringType),
        th.Property("u_transfer_notes", th.StringType),
        th.Property("u_transfer_requirements", th.StringType),
        th.Property("u_transferred_to", th.StringType),
        th.Property("u_transform_of_priority_for_sdp_tickets", th.StringType),
        th.Property("u_transform", th.StringType),
        th.Property("universal_request", th.StringType),
        th.Property("upon_approval", th.StringType),
        th.Property("upon_reject", th.StringType),
        th.Property("urgency", th.StringType),
        th.Property("user_input", th.StringType),
        th.Property("watch_list", th.StringType),
        th.Property("work_end", th.StringType),
        th.Property("work_notes_list", th.StringType),
        th.Property("work_notes", th.StringType),
        th.Property("work_start", th.StringType),
        ).to_dict()

class InteractionStream(ServiceNowStream):
    """Define Interaction stream."""

    name = "interaction"
    path = "/api/now/table/interaction?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("active",th.BooleanType),
        th.Property("agent_average_response_time",th.DateTimeType),
        th.Property("agent_chat",th.BooleanType),
        th.Property("application",th.StringType),
        th.Property("assigned_at",th.DateTimeType),
        th.Property("assigned_to",th.StringType),
        th.Property("assignment_group",th.StringType),
        th.Property("auto_resolution",th.BooleanType),
        th.Property("caller_phone_number",th.StringType),
        th.Property("category",th.StringType),
        th.Property("channel_metadata_document",th.StringType),
        th.Property("channel_metadata_table",th.StringType),
        th.Property("channel_user_profile",th.StringType),
        th.Property("client_host",th.StringType),
        th.Property("client_session_id",th.StringType),
        th.Property("closed_at",th.DateTimeType),
        th.Property("closed_by",th.StringType),
        th.Property("company",th.StringType),
        th.Property("connect_support",th.BooleanType),
        th.Property("context_document",th.StringType),
        th.Property("context_table",th.StringType),
        th.Property("context",th.StringType),
        th.Property("csat_score",th.StringType),
        th.Property("direction",th.StringType),
        th.Property("duration",th.DateTimeType),
        th.Property("first_response_wait_time",th.DateTimeType),
        th.Property("handling_duration",th.DateTimeType),
        th.Property("help_request",th.BooleanType),
        th.Property("help_requested_conversation",th.BooleanType),
        th.Property("live_handoff_time",th.DateTimeType),
        th.Property("location",th.StringType),
        th.Property("number", th.StringType),
        th.Property("number",th.StringType),
        th.Property("opened_at",th.BooleanType),
        th.Property("opened_by",th.StringType),
        th.Property("opened_for",th.StringType),
        th.Property("parent",th.StringType),
        th.Property("provider_application",th.StringType),
        th.Property("recording_url",th.StringType),
        th.Property("requester_average_response_time",th.DateTimeType),
        th.Property("sentiment",th.StringType),
        th.Property("short_description",th.StringType),
        th.Property("state_changed_on",th.DateTimeType),
        th.Property("state_reason",th.StringType),
        th.Property("state",th.StringType),
        th.Property("subcategory",th.StringType),
        th.Property("subtype",th.StringType),
        th.Property("supervisor_joined_conversation",th.BooleanType),
        th.Property("sys_class_name",th.StringType),
        th.Property("sys_class_name",th.StringType),
        th.Property("sys_created_by",th.StringType),
        th.Property("sys_created_on",th.DateTimeType),
        th.Property("sys_domain",th.StringType),
        th.Property("sys_id",th.StringType),
        th.Property("sys_mod_count",th.StringType),
        th.Property("sys_tags",th.StringType),
        th.Property("sys_updated_by",th.StringType),
        th.Property("sys_updated_on",th.DateTimeType),
        th.Property("system_wrap_up",th.BooleanType),
        th.Property("transcript_download",th.BooleanType),
        # th.Property("transcript",th.StringType),
        th.Property("type",th.StringType),
        th.Property("user_language",th.StringType),
        th.Property("verified",th.BooleanType),
        th.Property("virtual_agent",th.BooleanType),
        th.Property("voice_used",th.BooleanType),
        th.Property("wait_time",th.DateTimeType),
        th.Property("work_notes",th.StringType),
        th.Property("wrap_up_duration",th.StringType),
    ).to_dict()

class KbUseStream(ServiceNowStream):
    """Define KbUse stream."""

    name = "kb_use"
    path = "/api/now/table/kb_use?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("article_summary", th.StringType),
        th.Property("article", th.StringType),
        th.Property("search_id", th.StringType),
        th.Property("session_id", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_domain", th.StringType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("times_viewed", th.StringType),
        th.Property("used", th.BooleanType),
        th.Property("user", th.StringType),
        th.Property("viewed", th.BooleanType),
        ).to_dict()

class ScReqItemStream(ServiceNowStream):
    """Define ScReqItem stream."""

    name = "sc_req_item"
    path = "/api/now/table/sc_req_item?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("active", th.BooleanType),
        th.Property("activity_due", th.StringType),
        th.Property("additional_assignee_list", th.StringType),
        th.Property("approval_history", th.StringType),
        th.Property("approval_set", th.StringType),
        th.Property("approval", th.StringType),
        th.Property("assigned_to", th.StringType),
        th.Property("assignment_group", th.StringType),
        th.Property("backordered", th.BooleanType),
        th.Property("billable", th.BooleanType),
        th.Property("business_duration", th.StringType),
        th.Property("business_service", th.StringType),
        th.Property("calendar_duration", th.StringType),
        th.Property("cat_item", th.StringType),
        th.Property("close_notes", th.StringType),
        th.Property("closed_at", th.StringType),
        th.Property("closed_by", th.StringType),
        th.Property("cmdb_ci", th.StringType),
        th.Property("comments_and_work_notes", th.StringType),
        th.Property("comments", th.StringType),
        th.Property("company", th.StringType),
        th.Property("configuration_item", th.StringType),
        th.Property("contact_type", th.StringType),
        th.Property("context", th.StringType),
        th.Property("contract", th.StringType),
        th.Property("correlation_display", th.StringType),
        th.Property("correlation_id", th.StringType),
        th.Property("description", th.StringType),
        th.Property("due_date", th.StringType),
        th.Property("escalation", th.StringType),
        th.Property("estimated_delivery", th.StringType),
        th.Property("expected_start", th.StringType),
        th.Property("follow_up", th.StringType),
        th.Property("group_list", th.StringType),
        th.Property("impact", th.StringType),
        th.Property("knowledge", th.BooleanType),
        th.Property("location", th.StringType),
        th.Property("made_sla", th.BooleanType),
        th.Property("number", th.StringType),
        th.Property("opened_at", th.DateTimeType),
        th.Property("opened_by", th.StringType),
        th.Property("order_guide", th.StringType),
        th.Property("order", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("price", th.StringType),
        th.Property("priority", th.StringType),
        th.Property("quantity_sourced", th.StringType),
        th.Property("quantity", th.StringType),
        th.Property("reassignment_count", th.StringType),
        th.Property("received", th.BooleanType),
        th.Property("recurring_frequency", th.StringType),
        th.Property("recurring_price", th.StringType),
        th.Property("request", th.StringType),
        th.Property("requested_for", th.StringType),
        th.Property("route_reason", th.StringType),
        th.Property("sc_catalog", th.StringType),
        th.Property("service_offering", th.StringType),
        th.Property("short_description", th.StringType),
        th.Property("skills", th.StringType),
        th.Property("sla_due", th.StringType),
        th.Property("sn_esign_document", th.StringType),
        th.Property("sn_esign_esignature_configuration", th.StringType),
        th.Property("sourced", th.BooleanType),
        th.Property("stage", th.StringType),
        th.Property("state", th.StringType),
        th.Property("sys_class_name", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_domain_path", th.StringType),
        th.Property("sys_domain", th.StringType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("task_effective_number", th.StringType),
        th.Property("time_worked", th.StringType),
        th.Property("u_converted_to", th.StringType),
        th.Property("u_due_date", th.StringType),
        th.Property("u_follow_up", th.StringType),
        th.Property("u_high_security", th.BooleanType),
        th.Property("u_incorrectly_converted", th.BooleanType),
        th.Property("u_initiated_from", th.StringType),
        th.Property("u_initiating_interaction", th.StringType),
        th.Property("u_received_email", th.StringType),
        th.Property("u_tier_1", th.BooleanType),
        th.Property("u_tier_2", th.BooleanType),
        th.Property("u_tier_3", th.BooleanType),
        th.Property("u_transferred_to", th.StringType),
        th.Property("universal_request", th.StringType),
        th.Property("upon_approval", th.StringType),
        th.Property("upon_reject", th.StringType),
        th.Property("urgency", th.StringType),
        th.Property("user_input", th.StringType),
        th.Property("watch_list", th.StringType),
        th.Property("work_end", th.StringType),
        th.Property("work_notes_list", th.StringType),
        th.Property("work_notes", th.StringType),
        th.Property("work_start", th.StringType),
        ).to_dict()

class SpLogStream(ServiceNowStream):
    """Define SpLog stream."""

    name = "sp_log"
    path = "/api/now/table/sp_log?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("count", th.StringType),
        th.Property("id", th.StringType),
        th.Property("page", th.StringType),
        th.Property("portal", th.StringType),
        th.Property("session_id", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("table", th.StringType),
        th.Property("text", th.StringType),
        th.Property("type", th.StringType),
        ).to_dict()

class SysDictionaryStream(ServiceNowStream):
    """Define SysDictionary stream."""

    name = "sys_dictionary"
    path = "/api/now/table/sys_dictionary?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("active", th.BooleanType),
        th.Property("array_denormalized", th.BooleanType),
        th.Property("array", th.BooleanType),
        th.Property("attributes", th.StringType),
        th.Property("audit", th.BooleanType),
        th.Property("calculation", th.StringType),
        th.Property("choice_field", th.StringType),
        th.Property("choice_table", th.StringType),
        th.Property("choice", th.StringType), # seems like NumberType but get: jsonschema.exceptions.ValidationError: '0' is not of type 'number', 'null'
        th.Property("column_label", th.StringType),
        th.Property("comments", th.StringType),
        th.Property("create_roles", th.StringType),
        th.Property("default_value", th.StringType),
        th.Property("defaultsort", th.StringType),
        th.Property("delete_roles", th.StringType),
        th.Property("dependent_on_field", th.StringType),
        th.Property("dependent", th.StringType),
        th.Property("display", th.BooleanType),
        th.Property("dynamic_creation_script", th.BooleanType),
        th.Property("dynamic_creation", th.StringType),
        th.Property("dynamic_default_value", th.StringType),
        th.Property("dynamic_ref_qual", th.StringType),
        th.Property("element_reference", th.BooleanType),
        th.Property("element", th.StringType),
        th.Property("foreign_database", th.StringType),
        th.Property("formula", th.StringType),
        th.Property("function_definition", th.StringType),
        th.Property("function_field", th.BooleanType),
        th.Property("internal_type", th.StringType),
        th.Property("mandatory", th.BooleanType),
        th.Property("max_length", th.StringType), # seems like NumberType but get: jsonschema.exceptions.ValidationError: '32' is not of type 'number', 'null'
        th.Property("next_element", th.StringType),
        th.Property("primary", th.BooleanType),
        th.Property("read_only", th.BooleanType),
        th.Property("read_roles", th.StringType),
        th.Property("reference_cascade_rule", th.StringType),
        th.Property("reference_floats", th.BooleanType),
        th.Property("reference_key", th.StringType),
        th.Property("reference_qual_condition", th.StringType),
        th.Property("reference_qual", th.StringType),
        th.Property("reference_type", th.StringType),
        th.Property("reference", th.StringType),
        th.Property("sizeclass", th.StringType),
        th.Property("spell_check", th.BooleanType),
        th.Property("staged", th.BooleanType),
        th.Property("sys_class_name", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_customer_update", th.BooleanType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType), # seems like NumberType but get: jsonschema.exceptions.ValidationError: '0' is not of type 'number', 'null'
        th.Property("sys_name", th.StringType),
        th.Property("sys_policy", th.StringType),
        th.Property("sys_replace_on_upgrade", th.BooleanType),
        th.Property("sys_update_name", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("table_reference", th.BooleanType),
        th.Property("text_index", th.BooleanType),
        th.Property("unique", th.BooleanType),
        th.Property("use_dependent_field", th.BooleanType),
        th.Property("use_dynamic_default", th.BooleanType),
        th.Property("use_reference_qualifier", th.StringType),
        th.Property("virtual_type", th.StringType),
        th.Property("virtual", th.BooleanType),
        th.Property("widget", th.StringType),
        th.Property("write_roles", th.StringType),
        th.Property("xml_view", th.BooleanType),
        ).to_dict()

class SysUserStream(ServiceNowStream):
    """Define SysUser stream."""

    name = "sys_user"
    path = "/api/now/table/sys_user?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("active", th.BooleanType),
        th.Property("email", th.StringType),
        th.Property("employee_number", th.StringType),
        th.Property("first_name", th.StringType),
        th.Property("last_name", th.StringType),
        th.Property("name", th.StringType),
        th.Property("sys_class_name", th.StringType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("user_name", th.StringType),
        ).to_dict()