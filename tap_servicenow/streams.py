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
        th.Property("active", th.StringType),
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
        # th.Property("description", th.StringType),
        th.Property("due_date", th.StringType),
        th.Property("escalation", th.StringType),
        th.Property("expected_start", th.StringType),
        th.Property("follow_up", th.StringType),
        th.Property("group_list", th.StringType),
        th.Property("impact", th.StringType),
        th.Property("incident_state", th.StringType),
        th.Property("knowledge", th.StringType),
        th.Property("location", th.StringType),
        th.Property("made_sla", th.StringType),
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
        th.Property("u_high_security", th.StringType),
        th.Property("u_ibm_ticket_last_modified", th.StringType),
        th.Property("u_ibm_ticket_number", th.StringType),
        th.Property("u_incorrectly_converted", th.StringType),
        th.Property("u_initiated_from", th.StringType),
        th.Property("u_initiating_interaction", th.StringType),
        th.Property("u_integer_1", th.StringType),
        th.Property("u_journal_1", th.StringType),
        th.Property("u_keep_open", th.StringType),
        th.Property("u_message_id", th.StringType),
        th.Property("u_offense_id", th.StringType),
        th.Property("u_received_device_model", th.StringType),
        th.Property("u_received_email", th.StringType),
        th.Property("u_responded_to", th.StringType),
        th.Property("u_string_1", th.StringType),
        th.Property("u_string_2", th.StringType),
        th.Property("u_string_3", th.StringType),
        th.Property("u_tier_1", th.StringType),
        th.Property("u_tier_2", th.StringType),
        th.Property("u_tier_3", th.StringType),
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
        th.Property("active", th.StringType),
        th.Property("agent_average_response_time", th.DateTimeType),
        th.Property("agent_chat", th.StringType),
        th.Property("application", th.StringType),
        th.Property("assigned_at", th.DateTimeType),
        th.Property("assigned_to", th.StringType),
        th.Property("assignment_group", th.StringType),
        th.Property("auto_resolution", th.StringType),
        th.Property("caller_phone_number", th.StringType),
        th.Property("category", th.StringType),
        th.Property("channel_metadata_document", th.StringType),
        th.Property("channel_metadata_table", th.StringType),
        th.Property("channel_user_profile", th.StringType),
        th.Property("client_host", th.StringType),
        th.Property("client_session_id", th.StringType),
        th.Property("closed_at", th.DateTimeType),
        th.Property("closed_by", th.StringType),
        th.Property("company", th.StringType),
        th.Property("connect_support", th.StringType),
        th.Property("context_document", th.StringType),
        th.Property("context_table", th.StringType),
        th.Property("context", th.StringType),
        th.Property("csat_score", th.StringType),
        th.Property("direction", th.StringType),
        th.Property("duration", th.DateTimeType),
        th.Property("first_response_wait_time", th.DateTimeType),
        th.Property("handling_duration", th.DateTimeType),
        th.Property("help_request", th.StringType),
        th.Property("help_requested_conversation", th.StringType),
        th.Property("live_handoff_time", th.DateTimeType),
        th.Property("location", th.StringType),
        th.Property("number", th.StringType),
        th.Property("number", th.StringType),
        th.Property("opened_at", th.StringType),
        th.Property("opened_by", th.StringType),
        th.Property("opened_for", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("provider_application", th.StringType),
        th.Property("recording_url", th.StringType),
        th.Property("requester_average_response_time", th.DateTimeType),
        th.Property("sentiment", th.StringType),
        th.Property("short_description", th.StringType),
        th.Property("state_changed_on", th.DateTimeType),
        th.Property("state_reason", th.StringType),
        th.Property("state", th.StringType),
        th.Property("subcategory", th.StringType),
        th.Property("subtype", th.StringType),
        th.Property("supervisor_joined_conversation", th.StringType),
        th.Property("sys_class_name", th.StringType),
        th.Property("sys_class_name", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_domain", th.StringType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("system_wrap_up", th.StringType),
        th.Property("transcript_download", th.StringType),
        th.Property("type", th.StringType),
        th.Property("user_language", th.StringType),
        th.Property("verified", th.StringType),
        th.Property("virtual_agent", th.StringType),
        th.Property("voice_used", th.StringType),
        th.Property("wait_time", th.DateTimeType),
        th.Property("work_notes", th.StringType),
        th.Property("wrap_up_duration", th.StringType),
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
        th.Property("used", th.StringType),
        th.Property("user", th.StringType),
        th.Property("viewed", th.StringType),
    ).to_dict()


class ScReqItemStream(ServiceNowStream):
    """Define ScReqItem stream."""

    name = "sc_req_item"
    path = "/api/now/table/sc_req_item?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("active", th.StringType),
        th.Property("activity_due", th.StringType),
        th.Property("additional_assignee_list", th.StringType),
        th.Property("approval_history", th.StringType),
        th.Property("approval_set", th.StringType),
        th.Property("approval", th.StringType),
        th.Property("assigned_to", th.StringType),
        th.Property("assignment_group", th.StringType),
        th.Property("backordered", th.StringType),
        th.Property("billable", th.StringType),
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
        th.Property("knowledge", th.StringType),
        th.Property("location", th.StringType),
        th.Property("made_sla", th.StringType),
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
        th.Property("received", th.StringType),
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
        th.Property("sourced", th.StringType),
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
        th.Property("u_high_security", th.StringType),
        th.Property("u_incorrectly_converted", th.StringType),
        th.Property("u_initiated_from", th.StringType),
        th.Property("u_initiating_interaction", th.StringType),
        th.Property("u_received_email", th.StringType),
        th.Property("u_tier_1", th.StringType),
        th.Property("u_tier_2", th.StringType),
        th.Property("u_tier_3", th.StringType),
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


class SCRequest(ServiceNowStream):
    """Define SysUser stream."""

    name = "sc_request"
    path = "/api/now/table/sc_request?sysparm_exclude_reference_link=true"
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
        th.Property("business_duration", th.DateTimeType),
        th.Property("business_service", th.StringType),
        th.Property("calendar_duration", th.StringType),
        th.Property("calendar_stc", th.StringType),
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
        th.Property("delivery_address", th.StringType),
        th.Property("description", th.StringType),
        th.Property("due_date", th.DateTimeType),
        th.Property("escalation", th.StringType),
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
        th.Property("order", th.StringType),
        th.Property("parent_interaction", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("price", th.StringType),
        th.Property("priority", th.StringType),
        th.Property("reassignment_count", th.StringType),
        th.Property("request_state", th.StringType),
        th.Property("requested_date", th.StringType),
        th.Property("requested_for", th.StringType),
        th.Property("route_reason", th.StringType),
        th.Property("service_offering", th.StringType),
        th.Property("short_description", th.StringType),
        th.Property("skills", th.StringType),
        th.Property("sla_due", th.StringType),
        th.Property("sn_esign_document", th.StringType),
        th.Property("sn_esign_esignature_configuration", th.StringType),
        th.Property("sourceable", th.BooleanType),
        th.Property("sourced", th.BooleanType),
        th.Property("special_instructions", th.StringType),
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


class SCTaskStream(ServiceNowStream):
    """Define SCTask stream."""

    name = "sc_task"
    path = "/api/now/table/sc_task?sysparm_exclude_reference_link=true"
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
        th.Property("business_service", th.StringType),
        th.Property("calendar_duration", th.StringType),
        th.Property("calendar_stc", th.StringType),
        th.Property("cat_item", th.StringType),
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
        th.Property("expected_start", th.DateTimeType),
        th.Property("follow_up", th.StringType),
        th.Property("group_list", th.StringType),
        th.Property("impact", th.StringType),
        th.Property("knowledge", th.BooleanType),
        th.Property("location", th.StringType),
        th.Property("made_sla", th.BooleanType),
        th.Property("number", th.StringType),
        th.Property("opened_at", th.DateTimeType),
        th.Property("opened_by", th.StringType),
        th.Property("order", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("priority", th.StringType),
        th.Property("reassignment_count", th.StringType),
        th.Property("request_item", th.StringType),
        th.Property("request", th.StringType),
        th.Property("route_reason", th.StringType),
        th.Property("sc_catalog", th.StringType),
        th.Property("service_offering", th.StringType),
        th.Property("short_description", th.StringType),
        th.Property("skills", th.StringType),
        th.Property("sla_due", th.StringType),
        th.Property("sn_esign_document", th.StringType),
        th.Property("sn_esign_esignature_configuration", th.StringType),
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
        th.Property("u_due_date", th.DateTimeType),
        th.Property("u_follow_up", th.StringType),
        th.Property("u_high_security", th.BooleanType),
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
        th.Property("work_end", th.DateTimeType),
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


class SysDbObjectStream(ServiceNowStream):
    """Define SysDbObject stream."""

    name = "sys_db_object"
    path = "/api/now/table/sys_db_object?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("access", th.StringType),
        th.Property("actions_access", th.StringType),
        th.Property("alter_access", th.StringType),
        th.Property("caller_access", th.StringType),
        th.Property("client_scripts_access", th.StringType),
        th.Property("configuration_access", th.StringType),
        th.Property("create_access_controls", th.StringType),
        th.Property("create_access", th.StringType),
        th.Property("delete_access", th.StringType),
        th.Property("extension_model", th.StringType),
        th.Property("is_extendable", th.StringType),
        th.Property("label", th.StringType),
        th.Property("live_feed_enabled", th.StringType),
        th.Property("name", th.StringType),
        th.Property("number_ref", th.StringType),
        th.Property("read_access", th.StringType),
        th.Property("scriptable_table", th.StringType),
        th.Property("super_class", th.StringType),
        th.Property("sys_class_code", th.StringType),
        th.Property("sys_class_name", th.StringType),
        th.Property("sys_class_path", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_customer_update", th.StringType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_name", th.StringType),
        th.Property("sys_policy", th.StringType),
        th.Property("sys_replace_on_upgrade", th.StringType),
        th.Property("sys_update_name", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("update_access", th.StringType),
        th.Property("user_role", th.StringType),
        th.Property("ws_access", th.StringType),
    ).to_dict()


class SysDictionaryStream(ServiceNowStream):
    """Define SysDictionary stream."""

    name = "sys_dictionary"
    path = "/api/now/table/sys_dictionary?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("active", th.StringType),
        th.Property("array_denormalized", th.StringType),
        th.Property("array", th.StringType),
        th.Property("attributes", th.StringType),
        th.Property("audit", th.StringType),
        th.Property("calculation", th.StringType),
        th.Property("choice_field", th.StringType),
        th.Property("choice_table", th.StringType),
        th.Property(
            "choice", th.StringType
        ),  # seems like NumberType but get: jsonschema.exceptions.ValidationError: '0' is not of type 'number', 'null'
        th.Property("column_label", th.StringType),
        th.Property("comments", th.StringType),
        th.Property("create_roles", th.StringType),
        th.Property("default_value", th.StringType),
        th.Property("defaultsort", th.StringType),
        th.Property("delete_roles", th.StringType),
        th.Property("dependent_on_field", th.StringType),
        th.Property("dependent", th.StringType),
        th.Property("display", th.StringType),
        th.Property("dynamic_creation_script", th.StringType),
        th.Property("dynamic_creation", th.StringType),
        th.Property("dynamic_default_value", th.StringType),
        th.Property("dynamic_ref_qual", th.StringType),
        th.Property("element_reference", th.StringType),
        th.Property("element", th.StringType),
        th.Property("foreign_database", th.StringType),
        th.Property("formula", th.StringType),
        th.Property("function_definition", th.StringType),
        th.Property("function_field", th.StringType),
        th.Property("internal_type", th.StringType),
        th.Property("mandatory", th.StringType),
        th.Property(
            "max_length", th.StringType
        ),  # seems like NumberType but get: jsonschema.exceptions.ValidationError: '32' is not of type 'number', 'null'
        th.Property("next_element", th.StringType),
        th.Property("primary", th.StringType),
        th.Property("read_only", th.StringType),
        th.Property("read_roles", th.StringType),
        th.Property("reference_cascade_rule", th.StringType),
        th.Property("reference_floats", th.StringType),
        th.Property("reference_key", th.StringType),
        th.Property("reference_qual_condition", th.StringType),
        th.Property("reference_qual", th.StringType),
        th.Property("reference_type", th.StringType),
        th.Property("reference", th.StringType),
        th.Property("sizeclass", th.StringType),
        th.Property("spell_check", th.StringType),
        th.Property("staged", th.StringType),
        th.Property("sys_class_name", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_customer_update", th.StringType),
        th.Property("sys_id", th.StringType),
        th.Property(
            "sys_mod_count", th.StringType
        ),  # seems like NumberType but get: jsonschema.exceptions.ValidationError: '0' is not of type 'number', 'null'
        th.Property("sys_name", th.StringType),
        th.Property("sys_policy", th.StringType),
        th.Property("sys_replace_on_upgrade", th.StringType),
        th.Property("sys_update_name", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("table_reference", th.StringType),
        th.Property("text_index", th.StringType),
        th.Property("unique", th.StringType),
        th.Property("use_dependent_field", th.StringType),
        th.Property("use_dynamic_default", th.StringType),
        th.Property("use_reference_qualifier", th.StringType),
        th.Property("virtual_type", th.StringType),
        th.Property("virtual", th.StringType),
        th.Property("widget", th.StringType),
        th.Property("write_roles", th.StringType),
        th.Property("xml_view", th.StringType),
    ).to_dict()


class SysUserGroup(ServiceNowStream):
    """Define SysUser stream."""

    name = "sys_user_group"
    path = "/api/now/table/sys_user_group?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("active", th.BooleanType),
        th.Property("cost_center", th.StringType),
        th.Property("default_assignee", th.StringType),
        th.Property("description", th.StringType),
        th.Property("email", th.StringType),
        th.Property("exclude_manager", th.BooleanType),
        th.Property("hourly_rate", th.StringType),
        th.Property("include_members", th.BooleanType),
        th.Property("manager", th.StringType),
        th.Property("name", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("source", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("type", th.StringType),
        th.Property("u_tier", th.StringType),
        th.Property("vendors", th.StringType),
    ).to_dict()


class SysUserStream(ServiceNowStream):
    """Define SysUser stream."""

    name = "sys_user"
    path = "/api/now/table/sys_user?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("active", th.StringType),
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


class SnTaHiringCoreJobRequisitionStream(ServiceNowStream):
    """Define sn_ta_hiring_core_job_requisition stream."""

    name = "sn_ta_hiring_core_job_requisition"
    path = "/api/now/table/sn_ta_hiring_core_job_requisition?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("active", th.StringType),
        th.Property("activity_due", th.StringType),
        th.Property("additional_assignee_list", th.StringType),
        th.Property("additional_location", th.StringType),
        th.Property("additional_notes", th.StringType),
        th.Property("ai_resolution_plan", th.StringType),
        th.Property("applicant_type", th.StringType),
        th.Property("approval_history", th.StringType),
        th.Property("approval", th.StringType),
        th.Property("assignment_group", th.StringType),
        th.Property("assigned_to", th.StringType),
        th.Property("ats_link", th.StringType),
        th.Property("business_duration", th.StringType),
        th.Property("business_service", th.StringType),
        th.Property("calendar_duration", th.StringType),
        th.Property("category", th.StringType),
        th.Property("certification", th.StringType),
        th.Property("close_notes", th.StringType),
        th.Property("closed_at", th.DateTimeType),
        th.Property("closed_by", th.StringType),
        th.Property("closure_notes", th.StringType),
        th.Property("closure_reason", th.StringType),
        th.Property("cmdb_ci", th.StringType),
        th.Property("comments", th.StringType),
        th.Property("company", th.StringType),
        th.Property("compensation_range", th.StringType),
        th.Property("contact_type", th.StringType),
        th.Property("contract", th.StringType),
        th.Property("correlation_display", th.StringType),
        th.Property("correlation_id", th.StringType),
        th.Property("cost_center", th.StringType),
        th.Property("department", th.StringType),
        th.Property("description", th.StringType),
        th.Property("due_date", th.StringType),
        th.Property("employment_type", th.StringType),
        th.Property("escalation", th.StringType),
        th.Property("expected_start", th.StringType),
        th.Property("follow_up", th.StringType),
        th.Property("functional_job_title", th.StringType),
        th.Property("group_list", th.StringType),
        th.Property("hiring_manager", th.StringType),
        th.Property("immigration_sponsorship", th.StringType),
        th.Property("impact", th.StringType),
        th.Property("job_description", th.StringType),
        th.Property("job_title", th.StringType),
        th.Property("knowledge", th.StringType),
        th.Property("location_flexibility", th.StringType),
        th.Property("made_sla", th.StringType),
        th.Property("min_yrs_experience", th.StringType),
        th.Property("minimum_qualification", th.StringType),
        th.Property("number", th.StringType),
        th.Property("on_hold", th.StringType),
        th.Property("on_hold_notes", th.StringType),
        th.Property("on_hold_reason", th.StringType),
        th.Property("opened_at", th.DateTimeType),
        th.Property("opened_by", th.StringType),
        th.Property("opened_for", th.StringType),
        th.Property("order", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("position_count", th.StringType),
        th.Property("posted_date", th.StringType),
        th.Property("preferred_companies", th.StringType),
        th.Property("preferred_job_title", th.StringType),
        th.Property("preferred_skills", th.StringType),
        th.Property("primary_location", th.StringType),
        th.Property("priority", th.StringType),
        th.Property("prompt_text", th.StringType),
        th.Property("reason_for_hire", th.StringType),
        th.Property("reassignment_count", th.StringType),
        th.Property("relocation_support", th.StringType),
        th.Property("require_approval", th.StringType),
        th.Property("required_skills", th.StringType),
        th.Property("route_reason", th.StringType),
        th.Property("seniority_level", th.StringType),
        th.Property("service_offering", th.StringType),
        th.Property("skills", th.StringType),
        th.Property("sla_due", th.StringType),
        th.Property("sn_ai_sentiment", th.StringType),
        th.Property("sn_esign_document", th.StringType),
        th.Property("sn_esign_esignature_configuration", th.StringType),
        th.Property("short_description", th.StringType),
        th.Property("state", th.StringType),
        th.Property("sys_class_name", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_domain", th.StringType),
        th.Property("sys_domain_path", th.StringType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("task_effective_number", th.StringType),
        th.Property("time_worked", th.StringType),
        th.Property("travel_requirement", th.StringType),
        th.Property("u_account", th.StringType),
        th.Property("u_aeq_record", th.StringType),
        th.Property("u_approver_comments", th.StringType),
        th.Property("u_backfilled_employee_name", th.StringType),
        th.Property("u_business_contact", th.StringType),
        th.Property("u_compensation_currency", th.StringType),
        th.Property("u_confidential", th.StringType),
        th.Property("u_contract_type", th.StringType),
        th.Property("u_converted_to", th.StringType),
        th.Property("u_due_date", th.StringType),
        th.Property("u_engagement", th.StringType),
        th.Property("u_external_job_title", th.StringType),
        th.Property("u_follow_up", th.StringType),
        th.Property("u_gapi_status", th.StringType),
        th.Property("u_geo_focus", th.StringType),
        th.Property("u_geography", th.StringType),
        th.Property("u_high_security", th.StringType),
        th.Property("u_initiated_from", th.StringType),
        th.Property("u_initiating_interaction", th.StringType),
        th.Property("u_internal_external_job_post", th.StringType),
        th.Property("u_job_profile", th.StringType),
        th.Property("u_major", th.StringType),
        th.Property("u_minor", th.StringType),
        th.Property("u_opportunity", th.StringType),
        th.Property("u_organization", th.StringType),
        th.Property("u_project_start", th.DateType),
        th.Property("u_received_email", th.StringType),
        th.Property("u_recent_approver", th.StringType),
        th.Property("u_recruiter", th.StringType),
        th.Property("u_role", th.StringType),
        th.Property("u_role_related_to", th.StringType),
        th.Property("u_slalom_location", th.StringType),
        th.Property("u_sold_role_hire_justification", th.StringType),
        th.Property("u_tier_1", th.StringType),
        th.Property("u_tier_2", th.StringType),
        th.Property("u_tier_3", th.StringType),
        th.Property("u_transferred_to", th.StringType),
        th.Property("u_workforce_taxonomy", th.StringType),
        th.Property("universal_request", th.StringType),
        th.Property("upon_approval", th.StringType),
        th.Property("upon_reject", th.StringType),
        th.Property("urgency", th.StringType),
        th.Property("user_input", th.StringType),
        th.Property("watch_list", th.StringType),
        th.Property("work_end", th.StringType),
        th.Property("work_notes", th.StringType),
        th.Property("work_start", th.StringType),
        th.Property("working_hours", th.StringType),
    ).to_dict()


class CmnCostCenterStream(ServiceNowStream):
    """Define cmn_cost_center stream."""

    name = "cmn_cost_center"
    path = "/api/now/table/cmn_cost_center?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("account_number", th.StringType),
        th.Property("available_for_use", th.StringType),
        th.Property("code", th.StringType),
        th.Property("controlling_area", th.StringType),
        th.Property("cost_center_type", th.StringType),
        th.Property("location", th.StringType),
        th.Property("manager", th.StringType),
        th.Property("name", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_domain", th.StringType),
        th.Property("sys_domain_path", th.StringType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("u_active", th.StringType),
        th.Property("u_active_from", th.DateType),
        th.Property("u_active_until", th.StringType),
        th.Property("u_asset_eligible", th.StringType),
        th.Property("u_cost_center_number", th.StringType),
        th.Property("u_department", th.StringType),
        th.Property("u_engagement_eligible", th.StringType),
        th.Property("u_function_id", th.StringType),
        th.Property("u_gtm_country_region_id", th.StringType),
        th.Property("u_gtm_country_region_name", th.StringType),
        th.Property("u_gtm_market_id", th.StringType),
        th.Property("u_gtm_market_name", th.StringType),
        th.Property("u_legal_entity", th.StringType),
        th.Property("u_notes", th.StringType),
        th.Property("u_organization", th.StringType),
        th.Property("u_people_alignment", th.StringType),
        th.Property("u_people_eligible", th.StringType),
        th.Property("u_revenue_eligible", th.StringType),
        th.Property("u_type", th.StringType),
        th.Property("valid_from", th.StringType),
        th.Property("valid_to", th.StringType),
    ).to_dict()


class UXlkSalesforceEngagementsStream(ServiceNowStream):
    """Define u_xlk_salesforce_engagements stream."""

    name = "u_xlk_salesforce_engagements"
    path = "/api/now/table/u_xlk_salesforce_engagements?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("u_account", th.StringType),
        th.Property("u_acct_exec_lead", th.StringType),
        th.Property("u_active", th.StringType),
        th.Property("u_aeq_initiated_from", th.StringType),
        th.Property("u_contracting_entity", th.StringType),
        th.Property("u_cost_center", th.StringType),
        th.Property("u_external_date_updated", th.DateTimeType),
        th.Property("u_gsa_worktype", th.StringType),
        th.Property("u_last_sync", th.DateTimeType),
        th.Property("u_object_health", th.StringType),
        th.Property("u_object_id", th.StringType),
        th.Property("u_object_name", th.StringType),
        th.Property("u_object_status", th.StringType),
        th.Property("u_object_type", th.StringType),
        th.Property("u_opportunity", th.StringType),
        th.Property("u_parent", th.StringType),
        th.Property("u_platform", th.StringType),
        th.Property("u_salesforce_parent", th.StringType),
        th.Property("u_tpa_name", th.StringType),
        th.Property("u_type", th.StringType),
    ).to_dict()


class UXlkTaxonomyGeographiesStream(ServiceNowStream):
    """Define u_xlk_taxonomy_geographies stream."""

    name = "u_xlk_taxonomy_geographies"
    path = (
        "/api/now/table/u_xlk_taxonomy_geographies?sysparm_exclude_reference_link=true"
    )
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("u_active", th.StringType),
        th.Property("u_aeq_initiated_from", th.StringType),
        th.Property("u_external_date_updated", th.StringType),
        th.Property("u_geo_focus_eligible", th.StringType),
        th.Property("u_idl1", th.StringType),
        th.Property("u_idl2", th.StringType),
        th.Property("u_idl3", th.StringType),
        th.Property("u_idl4", th.StringType),
        th.Property("u_idl5", th.StringType),
        th.Property("u_idl6", th.StringType),
        th.Property("u_idl7", th.StringType),
        th.Property("u_idl8", th.StringType),
        th.Property("u_last_sync", th.DateTimeType),
        th.Property("u_level", th.StringType),
        th.Property("u_namepath", th.StringType),
        th.Property("u_nearest_location_eligible", th.StringType),
        th.Property("u_object_health", th.StringType),
        th.Property("u_object_id", th.StringType),
        th.Property("u_object_name", th.StringType),
        th.Property("u_object_status", th.StringType),
        th.Property("u_object_type", th.StringType),
        th.Property("u_parent", th.StringType),
        th.Property("u_people_eligible", th.StringType),
        th.Property("u_platform", th.StringType),
        th.Property("u_recruiting_eligible", th.StringType),
        th.Property("u_sales_eligible", th.StringType),
        th.Property("u_saleseligiblechildren", th.StringType),
        th.Property("u_short_name", th.StringType),
    ).to_dict()


class UExternalLookupKeyStream(ServiceNowStream):
    """Define u_external_lookup_key stream."""

    name = "u_external_lookup_key"
    path = "/api/now/table/u_external_lookup_key?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("u_active", th.StringType),
        th.Property("u_aeq_initiated_from", th.StringType),
        th.Property("u_external_date_updated", th.DateTimeType),
        th.Property("u_last_sync", th.DateTimeType),
        th.Property("u_object_health", th.StringType),
        th.Property("u_object_id", th.StringType),
        th.Property("u_object_name", th.StringType),
        th.Property("u_object_status", th.StringType),
        th.Property("u_object_type", th.StringType),
        th.Property("u_platform", th.StringType),
    ).to_dict()


class UXlkSalesforceOpportunitiesStream(ServiceNowStream):
    """Define u_xlk_salesforce_opportunities stream."""

    name = "u_xlk_salesforce_opportunities"
    path = "/api/now/table/u_xlk_salesforce_opportunities?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("u_account", th.StringType),
        th.Property("u_acct_exec_lead", th.StringType),
        th.Property("u_active", th.StringType),
        th.Property("u_aeq_initiated_from", th.StringType),
        th.Property("u_city_state_province", th.StringType),
        th.Property("u_cost_center", th.StringType),
        th.Property("u_crossborder_eligible", th.StringType),
        th.Property("u_customer_outcome", th.StringType),
        th.Property("u_customer_site", th.StringType),
        th.Property("u_engagement", th.StringType),
        th.Property("u_engagement_request", th.StringType),
        th.Property("u_external_date_updated", th.DateTimeType),
        th.Property("u_function", th.StringType),
        th.Property("u_geography", th.StringType),
        th.Property("u_last_sync", th.DateTimeType),
        th.Property("u_legal_entity", th.StringType),
        th.Property("u_object_health", th.StringType),
        th.Property("u_object_id", th.StringType),
        th.Property("u_object_name", th.StringType),
        th.Property("u_object_status", th.StringType),
        th.Property("u_object_type", th.StringType),
        th.Property("u_opportunity_value", th.StringType),
        th.Property("u_organization", th.StringType),
        th.Property("u_platform", th.StringType),
        th.Property("u_pursuit_lead", th.StringType),
        th.Property("u_relationship_lead", th.StringType),
        th.Property("u_sales_solution_lead", th.StringType),
        th.Property("u_slalom_capability", th.StringType),
        th.Property("u_slalom_geography", th.StringType),
        th.Property("u_stage", th.StringType),
        th.Property("u_street", th.StringType),
        th.Property("u_subtype", th.StringType),
        th.Property("u_type", th.StringType),
    ).to_dict()


class SnHrCorePeopleRolesStream(ServiceNowStream):
    """Define sn_hr_core_people_roles stream."""

    name = "sn_hr_core_people_roles"
    path = "/api/now/table/sn_hr_core_people_roles?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("u_active", th.StringType),
        th.Property("u_role_id", th.StringType),
        th.Property("u_role_name", th.StringType),
        th.Property("u_synced_by", th.StringType),
    ).to_dict()


class SnHrCoreJobProfileStream(ServiceNowStream):
    """Define sn_hr_core_job_profile stream."""

    name = "sn_hr_core_job_profile"
    path = "/api/now/table/sn_hr_core_job_profile?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("correlation_id", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_domain", th.StringType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("u_active", th.StringType),
        th.Property("u_job_family", th.StringType),
        th.Property("u_job_family_group", th.StringType),
        th.Property("u_job_level", th.StringType),
        th.Property("u_profile_id", th.StringType),
        th.Property("u_profile_name", th.StringType),
        th.Property("u_synced_by", th.StringType),
    ).to_dict()


class CmnLocationStream(ServiceNowStream):
    """Define cmn_location stream."""

    name = "cmn_location"
    path = "/api/now/table/cmn_location?sysparm_exclude_reference_link=true"
    primary_keys: t.ClassVar[list[str]] = ["sys_id"]
    replication_key = "sys_updated_on"
    is_sorted = True
    schema = th.PropertiesList(
        th.Property("city", th.StringType),
        th.Property("cmn_location_source", th.StringType),
        th.Property("cmn_location_type", th.StringType),
        th.Property("company", th.StringType),
        th.Property("contact", th.StringType),
        th.Property("coordinates_retrieved_on", th.StringType),
        th.Property("correlation_id", th.StringType),
        th.Property("duplicate", th.StringType),
        th.Property("fax_phone", th.StringType),
        th.Property("full_name", th.StringType),
        th.Property("lat_long_error", th.StringType),
        th.Property("latitude", th.StringType),
        th.Property("life_cycle_stage", th.StringType),
        th.Property("life_cycle_stage_status", th.StringType),
        th.Property("longitude", th.StringType),
        th.Property("managed_by_group", th.StringType),
        th.Property("name", th.StringType),
        th.Property("parent", th.StringType),
        th.Property("parent_hp1", th.StringType),
        th.Property("phone", th.StringType),
        th.Property("phone_territory", th.StringType),
        th.Property("primary_location", th.StringType),
        th.Property("state", th.StringType),
        th.Property("stock_room", th.StringType),
        th.Property("street", th.StringType),
        th.Property("sys_created_by", th.StringType),
        th.Property("sys_created_on", th.DateTimeType),
        th.Property("sys_id", th.StringType),
        th.Property("sys_mod_count", th.StringType),
        th.Property("sys_tags", th.StringType),
        th.Property("sys_updated_by", th.StringType),
        th.Property("sys_updated_on", th.DateTimeType),
        th.Property("time_zone", th.StringType),
        th.Property("u_abbreviation", th.StringType),
        th.Property("u_active", th.StringType),
        th.Property("u_active_from", th.StringType),
        th.Property("u_active_until", th.StringType),
        th.Property("u_address_line_2", th.StringType),
        th.Property("u_aeq_initiated_from", th.StringType),
        th.Property("u_country", th.StringType),
        th.Property("u_countryisoalpha2", th.StringType),
        th.Property("u_countryisoalpha3", th.StringType),
        th.Property("u_geo_taxonomy_id", th.StringType),
        th.Property("u_hierarchy_level", th.StringType),
        th.Property("u_ismetro", th.StringType),
        th.Property("u_ispeopleeligible", th.StringType),
        th.Property("u_local_area", th.StringType),
        th.Property("u_locale", th.StringType),
        th.Property("u_location_id", th.StringType),
        th.Property("u_posting_allowed", th.StringType),
        th.Property("u_set_by", th.StringType),
        th.Property("u_sla_schedule_gpt", th.StringType),
        th.Property("u_state_province_code", th.StringType),
        th.Property("u_type", th.StringType),
        th.Property("zip", th.StringType),
    ).to_dict()
