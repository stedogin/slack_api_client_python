from slack_apps_client import send_command_to_channel


def test_slash_command_internal_parsing():
    message_result = send_command_to_channel("/action_endpoint", "test")

    assert message_result.get("ok") is True
