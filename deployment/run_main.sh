#!/usr/bin/env bash
source "${HOME}/thenaivemind/slack_api_client_python_venv/bin/activate"
export PYTHONPATH="${PYTHONPATH}:${HOME}/thenaivemind/slack_api_client_python/source"
python3.7 -B "${HOME}/thenaivemind/slack_api_client_python/source/main.py"
