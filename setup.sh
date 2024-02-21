#!/usr/bin/env bash

DNAME="$1"
echo $DNAME

python -m venv "venv/$DNAME"

source "venv/$DNAME/bin/activate
pip install --upgrade pip && pip install -r backend/requirements.txt