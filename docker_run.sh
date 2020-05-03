sudo docker container rm --force pp
sudo docker image build -t pastebin_project:1.0 .
sudo docker container run -t -d \
    -v /var/run/postgresql:/var/run/postgresql \
    -e PW_pastebin_project=$PW_pastebin_project \
    --network host --detach --name pp pastebin_project:1.0
sudo docker exec -it pp bash