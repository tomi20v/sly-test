#!/bin/sh
source .venv/bin/activate
python -u -m flask --app app.main run --debug