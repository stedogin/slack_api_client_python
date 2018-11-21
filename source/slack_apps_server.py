from flask import Flask, request, Response
from slack_apps_utils import is_valid_request


UNAUTHORIZED_RESPONSE = Response("Unauthorized request: please check the SLACK_SIGNING_SECRET environment variable.")

slack_apps_server = Flask(__name__)


@slack_apps_server.route("/action_endpoint", methods=["POST"])
def run_slack_action():
    if is_valid_request(request):
        # request_payload_dict = json.loads(request.form["payload"])
        raw_request_arguments = request.form.get("text")
        if raw_request_arguments == "":
            return Response("Missing input, please try again")

        return Response("Done")

    else:
        return UNAUTHORIZED_RESPONSE


@slack_apps_server.route('/', methods=["POST", "GET"])
def test_endpoint():
    if request.method == "POST":
        print(request.data)
        return Response(request.data)

    if request.method == "GET":
        print("/slack endpoint online")
        return Response("/slack endpoint online")


if __name__ == "__main__":
    slack_apps_server.run(debug=True)
