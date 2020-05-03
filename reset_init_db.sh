export APP_SETTINGS="db_config.DevelopmentConfig"
export DATABASE_URL="postgresql:///pastebin_project"

sudo service postgresql start

python3 backend/reset_init_db.py