.SILENT:
VENV_NAME := .venv
APP_NAME := casa-planner
PACK_DESTINATION := ../pack
PACK_NAME := casa_planner.tar

pythonpath:
	export PYTHONPATH=.

run dev:pythonpath
	$(VENV_NAME)/bin/python3 main.py

run prod:pythonpath
	export CASAPLANNER_CONFIG=DefaultConfig && $(VENV_NAME)/bin/python3 main.py

venv:
	sh bin/venv.sh . $(VENV_NAME)

install dev:
	$(VENV_NAME)/bin/pip3 install -r requirements/development.txt

test unit:pythonpath
	sh bin/test.sh $(VENV_NAME) 'unit'

test functional:pythonpath
	sh bin/test.sh $(VENV_NAME) 'functional'

setup:
	sh bin/setup.sh ".bash_profile"

clean:
	sh bin/clean.sh . '__pycache__'
	sh bin/clean.sh tests '.cache'

pack:clean
	sh bin/pack.sh $(APP_NAME) $(PACK_DESTINATION) $(PACK_NAME)

deploy:
	sh bin/deploy.sh '$(PACK_DESTINATION)/$(PACK_NAME)'

migration init:pythonpath
	alembic init migrations

migration create:pythonpath
	sh bin/migrate.sh

migration apply:pythonpath
	alembic upgrade head
