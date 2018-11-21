from slack_message_utils import slack_list, slack_button, create_response, create_interactive_message_attachment, \
    parse_list_values_for_slack


def test_slack_button():
    result_button = slack_button("name", "text", "value")
    assert result_button == {"name": "name",
                             "text": "text",
                             "value": "value",
                             "type": "button",
                             "style": ""}


def test_slack_list_no_selected_options():
    result_list = slack_list("name", "text", ["option1", "option2"])
    assert result_list == {"name": "name",
                           "text": "text",
                           "options": ["option1", "option2"],
                           "selected_options": None,
                           "type": "select",
                           "data_source": "static"}


def test_slack_list_with_selected_options():
    result_list = slack_list("name", "text", ["option1", "option2"], selected_options=["option1"])
    assert result_list == {"name": "name",
                           "text": "text",
                           "options": ["option1", "option2"],
                           "selected_options": ["option1"],
                           "type": "select",
                           "data_source": "static"}


def test_parse_list_values_for_slack():
    values = ["option1", "option2"]
    parsed_values = parse_list_values_for_slack(values)

    assert parsed_values == [{"text": "option1", "value": "option1"}, {"text": "option2", "value": "option2"}]


def test_create_interactive_message_attachment():
    values = ["option1", "option2"]
    parsed_values = parse_list_values_for_slack(values)
    actions = [slack_list("test_list_name",
                          "test_list_text",
                          parsed_values),
               slack_button("test_button_name",
                            "test_button_text",
                            "text_button_value")]
    result_attachment = create_interactive_message_attachment("callback_id", "title", "text", "fallout", actions)

    assert result_attachment == {"callback_id": "callback_id",
                                 "title": "title",
                                 "text": "text",
                                 "fallout": "fallout",
                                 "actions": [{"name": "test_list_name",
                                              "text": "test_list_text",
                                              "options": [{"text": "option1", "value": "option1"},
                                                          {"text": "option2", "value": "option2"}],
                                              "selected_options": None,
                                              "type": "select",
                                              "data_source": "static"},
                                             {"name": "test_button_name",
                                              "text": "test_button_text",
                                              "value": "text_button_value",
                                              "type": "button",
                                              "style": ""}]}


def test_create_response_no_attachments():
    result_response = create_response("title", "text")
    assert result_response == {"title": "title", "text": "text", "attachments": None}


def test_create_response_with_attachments():
    values = ["option1", "option2"]
    parsed_values = parse_list_values_for_slack(values)
    actions = [slack_list("test_list_name",
                          "test_list_text",
                          parsed_values),
               slack_button("test_button_name",
                            "test_button_text",
                            "text_button_value")]
    result_attachment = create_interactive_message_attachment("callback_id", "title", "text", "fallout", actions)
    result_response = create_response("title", "text", [result_attachment])

    assert result_response == {'title': 'title',
                               'text': 'text',
                               'attachments': [{'callback_id': 'callback_id',
                                                'title': 'title',
                                                'text': 'text',
                                                'fallout': 'fallout',
                                                'actions': [{'name': 'test_list_name',
                                                             'text': 'test_list_text',
                                                             'options': [{'text': 'option1', 'value': 'option1'},
                                                                         {'text': 'option2', 'value': 'option2'}],
                                                             'selected_options': None,
                                                             'type': 'select',
                                                             'data_source': 'static'},
                                                            {'name': 'test_button_name',
                                                             'text': 'test_button_text',
                                                             'value': 'text_button_value',
                                                             'type': 'button', 'style': ''}]}]}
