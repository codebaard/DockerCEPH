#!/bin/sh

docker ps -a | grep ceph | xargs docker stop | xargs docker rm

exit 0
