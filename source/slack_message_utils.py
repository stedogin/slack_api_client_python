from typing import List


SLACK_BUTTON_TYPE = "button"
SLACK_SELECT_LIST_TYPE = "select"


def slack_button(name, text, value):
    return {
        "name": name,
        "text": text,
        "value": value,
        "type": "button",
        "style": ""
    }


def slack_list(name, text, options: List, selected_options: List=None):
    return {
        "name": name,
        "text": text,
        "options": options,
        "selected_options": selected_options,
        "type": "select",
        "data_source": "static"
    }


def create_interactive_message_attachment(callback_id: str, title, text, fallout: str, actions: List):
    return {
        "callback_id": callback_id,
        "title": title,
        "text": text,
        "fallout": fallout,
        "actions": actions
    }


def create_response(title="", text="", attachments: List=None):
    return {
        "title": title,
        "text": text,
        "attachments": attachments
    }


def parse_list_values_for_slack(values):
    parsed_list = [{"text": value, "value": value} for value in values]
    return parsed_list
