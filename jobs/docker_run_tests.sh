#!/bin/sh

docker stop ht4_mic_ped
docker rm ht4_mic_ped
docker run --name=ht4_mic_ped --net=host ht4_mic_ped python /code/pedidos/test.py