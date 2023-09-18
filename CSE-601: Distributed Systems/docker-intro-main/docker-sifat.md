docker images
groups borovai
sudo usermod -aG docker ${USER}
sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker
docker run hello-world
docker images
