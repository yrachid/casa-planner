#! /bin/bash
SCRIPT_ROOT=$1
VENV_NAME=$2

if [ ! -d "$SCRIPT_ROOT/$VENV_NAME" ]; then
    pip3 install virtualenv
    mkdir $VENV_NAME
    python -m venv $VENV_NAME
    $VENV_NAME/bin/pip3 install --upgrade pip
    $VENV_NAME/bin/pip3 install --upgrade setuptools
else
    echo 'Virtualenv already created. Run: "source .venv/bin/activate" to use it'
fi
echo 'Done'
