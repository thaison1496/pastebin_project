# Used by Docker CMD
# Need docker to run with --network host (share ip) for 127.0.0.1 to work
export APP_SETTINGS="db_config.DevelopmentConfig"
export DATABASE_URL="postgresql://pastebin_project:$PW_pastebin_project@127.0.0.1/pastebin_project"

mkdir logs
nginx -p nginx/ -c nginx.conf
cd backend; gunicorn3 --reload -w 1 -b localhost:5051 app:app >> ../logs/gunicorn.log 2>&1 &