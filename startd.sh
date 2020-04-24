export APP_SETTINGS="db_config.DevelopmentConfig"
export DATABASE_URL="postgresql:///pastebin_project"

sudo service postgresql start
nginx -p nginx/ -c nginx.conf
cd backend; gunicorn3 -w 1 -b localhost:5051 app:app >> ../logs/gunicorn.log 2>&1 &