#!/bin/sh

docker run -d --name=ht4_mic_ped --net=host ht4_mic_ped python /code/pedidos/main.py