#!/bin/bash

repo_root="$(dirname "$0")" # get the script's directory

python -m venv ${repo_root}/venv

source ${repo_root}/venv/bin/activate

pip install -r ${repo_root}/requirements.txt

deactivate

