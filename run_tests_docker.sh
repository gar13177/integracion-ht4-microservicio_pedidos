#!/bin/sh

docker stop ht4_mic_tests
docker rm ht4_mic_tests
docker rmi ht4_mic_tests
docker build . -t ht4_mic_tests
docker run --name ht4_mic_tests ht4_mic_tests python /code/pedidos/test.py