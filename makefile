.SILENT:
VENV_NAME := .venv
APP_NAME := casa-planner
PACK_DESTINATION := ../pack
PACK_NAME := casa_planner.zip

run dev:
	export PYTHONPATH=. && $(VENV_NAME)/bin/python3 main.py

run prod:
	export PYTHONPATH=. && export CASAPLANNER_CONFIG=DefaultConfig && $(VENV_NAME)/bin/python3 main.py

venv:
	sh bin/venv.sh . $(VENV_NAME)

install dev:
	$(VENV_NAME)/bin/pip3 install -r requirements/development.txt

test unit:
	export PYTHONPATH=. && sh bin/test.sh $(VENV_NAME) 'unit'

test functional:
	export PYTHONPATH=. && sh bin/test.sh $(VENV_NAME) 'functional'

setup:
	sh bin/setup.sh ".bash_profile"

clean:
	sh bin/clean.sh . '__pycache__'
	sh bin/clean.sh tests '.cache'

pack:clean
	sh bin/pack.sh $(APP_NAME) $(PACK_DESTINATION) $(PACK_NAME)

deploy:
	sh -x bin/deploy.sh $(PACK_DESTINATION) $(PACK_NAME)

migration init:
	export PYTHONPATH=. && alembic init migrations

migration create:
	export PYTHONPATH=. && sh bin/migrate.sh

migration apply:
	export PYTHONPATH=. && alembic upgrade head

migration rollback:
	export PYTHONPATH=. && alembic downgrade base
