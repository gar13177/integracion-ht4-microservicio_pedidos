#!/bin/sh

docker stop ht4_mic_ped
docker rm ht4_mic_ped
docker rmi ht4_mic_ped
docker build . -t ht4_mic_ped 
docker run -d --name ht4_mic_ped --net=host ht4_mic_ped python /code/pedidos/main.py