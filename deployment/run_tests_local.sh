#!/usr/bin/env bash
source "${HOME}/thenaivemind/slack_api_client_python_venv/bin/activate"
export PYTHONPATH="${PYTHONPATH}:${HOME}/thenaivemind/slack_api_client_python/source"
cd "${HOME}/thenaivemind/slack_api_client_python/source"
pytest -v ../tests/