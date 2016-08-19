echo 'Migration message:'
read MESSAGE

alembic revision --autogenerate -m "$MESSAGE"
