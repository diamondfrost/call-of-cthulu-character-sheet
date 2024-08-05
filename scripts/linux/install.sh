#!/bin/bash

VIRTUAL_ENV="coc-sheet-env"
if [ ! -f $VIRTUAL_ENV/bin/activate ]; then
    pip install virtualenv
    python3 -m venv $VIRTUAL_ENV
fi

if [ ! -f $VIRTUAL_ENV/bin/activate ]; then
    exit
fi

source coc-sheet-env/bin/activate
pip install -r requirements.txt