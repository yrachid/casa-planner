function export_variable() {
    echo "export $1=$2" >> "~/$3"
}

DESTINATION_FILE=$1

if [ -z "$SYRUP_DATABASE_URL" ]; then

    echo "[Application connection String setup]"

    echo "Type the database username:"
    read DB_USER

    echo "Type the database password:"
    read DB_PASSWORD

    echo "Type the database name:"
    read DB_NAME

    export_variable "SYRUP_DATABASE_URL" "$DB_USER:$DB_PASSWORD@localhost:5432/$DB_NAME" "$DESTINATION_FILE"

    echo "[Database connection string set]"
else
    echo "Database connection string already configured"
fi

echo "Done"
