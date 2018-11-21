import os
from slackclient import SlackClient


SLACK_DEFAULT_MESSAGE = "Ping!"
SLACK_DEFAULT_CHANNEL_ID = "CD8J99V41"
SLACK_DEFAULT_ICON = ":space_invader:"
SLACK_DEFAULT_DISPLAY_NAME = "SLACK-APP-TEST"


slack_client = SlackClient(os.environ["SLACK_OAUTH_ACCESS_TOKEN"])
legacy_slack_client = SlackClient(os.environ["SLACK_LEGACY_TOKEN"])


def get_channel_ids_by_names():
    api_call_result = slack_client.api_call(method="channels.list")
    channel_ids_by_names = {}
    if api_call_result["ok"]:
        channels_data = api_call_result["channels"]
        channel_ids_by_names = {channel["name"]: channel["id"] for channel in channels_data
                                if not channel["is_archived"]}
    return channel_ids_by_names


def get_channel_id_from_name(channel_name):
    channel_ids_by_names = get_channel_ids_by_names()
    channel_id = channel_ids_by_names[channel_name]
    return channel_id


def send_message_to_channel(message=SLACK_DEFAULT_MESSAGE, attachments=None,
                            channel_id=SLACK_DEFAULT_CHANNEL_ID, icon=SLACK_DEFAULT_ICON,
                            display_name=SLACK_DEFAULT_DISPLAY_NAME):
    result = slack_client.api_call(method="chat.postMessage", text=message, attachments=attachments,
                                   icon_emoji=icon, channel=channel_id, username=display_name)
    return result


def send_command_to_channel(command, arguments=None):
    result = legacy_slack_client.api_call(method="chat.command", command=command, text=arguments,
                                          channel=SLACK_DEFAULT_CHANNEL_ID)
    return result


def send_message_to_user(message, user_name):
    # api_call_result = slack_client.api_call(method="im.open")
    # if api_call_result["ok"]:
    #     im_channel_id = api_call_result.channel["id"]
    #     send_message_to_channel(message=message, channel_id=im_channel_id)
    pass
