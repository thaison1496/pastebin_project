nginx -p nginx/ -c nginx.conf -s stop
kill $(lsof -t -i:5051)