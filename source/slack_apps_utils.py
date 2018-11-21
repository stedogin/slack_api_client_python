import os
import hmac
from hashlib import sha256
from urllib.parse import urlencode


def is_valid_request(request):
    request_body = urlencode(request.form)
    request_headers = request.headers
    request_timestamp = str(request_headers["X-Slack-Request-Timestamp"])
    request_signature = request_headers["X-Slack-Signature"]
    request_version, _ = str(request_signature).split('=')

    # TODO: validate recent timestamp for replay attacks

    validation_hash_key = os.environ["SLACK_SIGNING_SECRET"]
    validation_hash_message = "v0:" + request_timestamp + ':' + request_body
    validation_hexdigest = hmac.new(key=str.encode(validation_hash_key),
                                    msg=str.encode(validation_hash_message), digestmod=sha256).hexdigest()
    validation_result = f"{request_version}={validation_hexdigest}"

    return hmac.compare_digest(validation_result, request_signature)


class SimulatedSlackRequest:
    def __init__(self, headers, form):
        self.headers = headers
        self.form = form
