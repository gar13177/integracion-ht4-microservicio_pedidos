#!/bin/sh

sudo docker stop ht4_mic_tests
sudo docker rm ht4_mic_tests
sudo docker rmi ht4_mic_tests
sudo docker build . -t ht4_mic_tests
sudo docker run --name ht4_mic_tests ht4_mic_tests python /code/pedidos/test.py