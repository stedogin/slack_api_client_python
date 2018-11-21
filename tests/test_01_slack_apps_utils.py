from werkzeug.datastructures import ImmutableMultiDict
from slack_apps_client import get_channel_id_from_name
from slack_apps_utils import SimulatedSlackRequest, is_valid_request


def test_get_channel_id_from_name():
    output_channel_name = "z-slack-app-test"
    output_channel_id = get_channel_id_from_name(output_channel_name)
    assert output_channel_id == "CD8J99V41"


def test_is_valid_request():
    request_headers = {"User-Agent": "Slackbot 1.0 (+https://api.slack.com/robots)",
                       "Accept-Encoding": "gzip,deflate",
                       "Accept": "application/json,*/*",
                       "X-Slack-Signature": "v0=dfa4f9d3c45a9a08474523beff63c72385ea1e079328953634de05bb2d6085fa",
                       "X-Slack-Request-Timestamp": "1539685691",
                       "Content-Length": "374",
                       "Content-Type": "application/x-www-form-urlencoded",
                       "Host": "slack-apps.superfly.com:5000",
                       "Cache-Control": "max-age=259200",
                       "Connection": "keep-alive"}
    request_form = ImmutableMultiDict([('token', '544pTOY3NRWVWHijgM8bcZ8M'),
                                       ('team_id', 'T02T1PGDE'),
                                       ('team_domain', 'superflyltd'),
                                       ('channel_id', 'CD8J99V41'),
                                       ('channel_name', 'z-slack-app-test'),
                                       ('user_id', 'UAM138DU7'),
                                       ('user_name', 'yoav.magor'),
                                       ('command', '/delivery_maker'),
                                       ('text', 'test'),
                                       ('response_url', 'https://hooks.slack.com/commands/T02T1PGDE/'
                                                        '458216560119/b60eFvo8XICmp4Qv0nOSnejc'),
                                       ('trigger_id', '456989048548.2919798456.b97e8f083e1b4f8be5069a50046da9c8')])
    simulated_request = SimulatedSlackRequest(request_headers, request_form)

    assert is_valid_request(simulated_request) is True
