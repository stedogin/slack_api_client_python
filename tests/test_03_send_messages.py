import json
import requests
from slack_apps_client import send_message_to_channel


DEFAULT_CHANNEL_ID = "CD8J99V41"
DEFAULT_EMOJI_ICON = ":space_invader:"
DEFAULT_DISPLAY_NAME = "SLACK-APP-TEST"

CHANNEL_WEBHOOK_URL = "https://hooks.slack.com/services/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"
USER_WEBHOOK_URL = "https://hooks.slack.com/services/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"


def test_send_message_to_channel_using_client():
    message_text = "test_send_message_to_channel_using_client"
    message_result = send_message_to_channel(message=message_text, attachments=None,
                                             channel_id=DEFAULT_CHANNEL_ID, icon=DEFAULT_EMOJI_ICON,
                                             display_name=DEFAULT_DISPLAY_NAME)
    assert message_result.get("ok") is True


def test_send_interactive_message_to_channel_using_client():
    interactive_message_text = "test_send_interactive_message_to_channel_using_client"
    interactive_message_attachment = json.dumps([
        {"fallback": "Plan a vacation",
         "author_name": "Owner: rdesoto",
         "title": "Plan a vacation",
         "text": "I've been working too hard, it's time for a break.",
         "actions": [
             {"name": "action",
              "type": "button",
              "text": "Complete this task",
              "style": "", "value": "complete"},
             {"name": "tags_list",
              "type": "select",
              "text": "Add a tag...",
              "data_source": "static",
              "options": [
                  {"text": "Launch Blocking",
                   "value": "launch-blocking"},
                  {"text": "Enhancement",
                   "value": "enhancement"},
                  {"text": "Bug",
                   "value": "bug"}
              ]}
         ]}
    ])
    interactive_message_result = send_message_to_channel(message=interactive_message_text,
                                                         attachments=interactive_message_attachment,
                                                         channel_id=DEFAULT_CHANNEL_ID,
                                                         icon=DEFAULT_EMOJI_ICON,
                                                         display_name=DEFAULT_DISPLAY_NAME)

    assert interactive_message_result.get("ok") is True


def test_send_message_to_user_using_client():
    # TODO: add test code
    pass


def test_send_message_to_channel_using_webhook():
    webhook_channel_message = {"text": "test_send_message_to_channel_using_webhook",
                               "username": "SLACK-WEBHOOK-TEXT-CHANNEL",
                               "icon_emoji": ":frog:"}

    webhook_channel_response = requests.post(CHANNEL_WEBHOOK_URL, data=str(webhook_channel_message),
                                             headers={"Content-Type": "application/json"})

    assert webhook_channel_response.ok is True


def test_send_interactive_message_to_channel_using_webhook():
    interactive_message = {"text": "test_send_interactive_message_to_channel_using_webhook",
                           "attachments": [
                               {"fallback": "Plan a vacation",
                                "author_name": "Owner: rdesoto",
                                "title": "Plan a vacation",
                                "text": "I've been working too hard, it's time for a break.",
                                "actions": [
                                    {"name": "action",
                                     "type": "button",
                                     "text": "Complete this task",
                                     "style": "",
                                     "value": "complete"},
                                    {"name": "tags_list",
                                     "type": "select",
                                     "text": "Add a tag...",
                                     "data_source": "static",
                                     "options": [
                                         {"text": "Launch Blocking",
                                          "value": "launch-blocking"},
                                         {"text": "Enhancement",
                                          "value": "enhancement"},
                                         {"text": "Bug",
                                          "value": "bug"}
                                     ]}
                                ]}
                           ]}
    webhook_interactive_response = requests.post(CHANNEL_WEBHOOK_URL, data=str(interactive_message),
                                                 headers={"Content-Type": "application/json"})

    assert webhook_interactive_response


def test_send_message_to_user_using_webhook():
    webhook_user_message = {"text": "test_send_message_to_user_using_webhook",
                            "username": DEFAULT_DISPLAY_NAME,
                            "icon_emoji": ":pig:"}

    webhook_user_response = requests.post(USER_WEBHOOK_URL, data=str(webhook_user_message),
                                          headers={"Content-Type": "application/json"})

    assert webhook_user_response.ok is True
