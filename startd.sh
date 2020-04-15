nginx -p nginx/ -c nginx.conf
gunicorn -w 1 -b localhost:5051 backend.app:app >> logs/gunicorn.log 2>&1 &