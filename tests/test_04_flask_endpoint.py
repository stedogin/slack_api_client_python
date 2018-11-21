import json
import requests


SLACK_APPS_ENDPOINT_URL = "http://slack-apps.superfly.com:5000/"


def test_endpoint_availability():
    endpoint_get_response = requests.get(SLACK_APPS_ENDPOINT_URL)

    assert endpoint_get_response.ok is True


def test_endpoint_parsing():
    endpoint_post_request_data = json.dumps([{"fallback": "test_fallback",
                                              "author_name": "test_author",
                                              "title": "test_title",
                                              "text": "test_text",
                                              "actions": [{
                                                  "name": "tags_list",
                                                  "type": "select",
                                                  "text": "select_text:",
                                                  "data_source": "static",
                                                  "options": [
                                                      {"text": "uber", "value": "select-uber"},
                                                      {"text": "gett", "value": "select-gett"},
                                                      {"text": "temasek", "value": "temasek"}]}]}])

    endpoint_post_response = requests.post(SLACK_APPS_ENDPOINT_URL, data=endpoint_post_request_data,
                                           headers={"Content-Type": "application/json"})

    assert endpoint_post_response.ok is True and \
           endpoint_post_response.text == endpoint_post_request_data
