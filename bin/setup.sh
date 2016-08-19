#!/bin/sh

function export_variable() {
    echo "export $1=$2" >> "/home/$(whoami)/$3"
}

DESTINATION_FILE=$1

if [ -z "$CASAPLANNER_DATABASE_URL" ]; then

    echo "[Application connection String setup]"

    echo "Type the database username:"
    read DB_USER

    echo "Type the database password:"
    read DB_PASSWORD

    echo "Type the database name:"
    read DB_NAME

    export_variable "CASAPLANNER_DATABASE_URL" "$DB_USER:$DB_PASSWORD@localhost:5432/$DB_NAME" "$DESTINATION_FILE"

    echo "[Database connection string set]"
else
    echo "Database connection string already configured"
fi

if [ -z "$CASAPLANNER_DEPLOY_HOST" ]; then
  echo "[Deployment host IP]"

  echo "Type the destination host ip:"
  read HOST_IP

  export_variable "CASAPLANNER_DEPLOY_HOST" "$HOST_IP" "$DESTINATION_FILE"

  echo "[Deployment host set]"
else
  echo "Deployment host already set"
fi

echo "Done"
