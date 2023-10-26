echo off
echo #################################################
echo docker-compose drop postgres
echo #################################################
docker-compose drop postgres

echo #################################################
echo docker-compose build
echo #################################################
docker-compose build

echo #################################################
echo docker-compose up
echo #################################################
docker-compose up