#!/bin/bash
set -e
python3 -m venv --upgrade-deps .venv
. .venv/bin/activate
python -m pip install -e . -r requirements-dev.txt
