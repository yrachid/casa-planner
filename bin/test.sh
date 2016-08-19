#!/bin/sh

VENV=$1
TEST_PATH=$2

$VENV/bin/pip3 install -r requirements/test.txt
$VENV/bin/py.test tests/$TEST_PATH
