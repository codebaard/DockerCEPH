#!/bin/sh

## start MON and MGR
docker run -d -v /docker/ceph/data/etc:/etc/ceph -v /docker/ceph/data/lib:/var/lib/ceph/ -e MON_IP=192.168.178.220 -e CEPH_PUBLIC_NETWORK=192.168.178.0/24 --ip=192.168.178.220 --network=macvlan0 --name ceph_mon1 ceph/daemon mon
docker run -d -v /docker/ceph/data/etc:/etc/ceph -v /docker/ceph/data/lib:/var/lib/ceph/ --ip=192.168.178.223 --network=macvlan0 --name ceph_mgr ceph/daemon mgr

docker exec -it ceph_mon1 ceph auth get client.bootstrap-osd -o /var/lib/ceph/bootstrap-osd/ceph.keyring

## prepare and create OSDs
./prepare.sh
./create.sh

## create fs
docker exec -it ceph_mon1 ceph osd pool create cephfs_data
docker exec -it ceph_mon1 ceph osd pool create cephfs_metadata
docker exec -it ceph_mon1 ceph fs new cephfs cephfs_metadata cephfs_data

##create the additional MON and MDS after the cluster has been created
docker run -d -v /docker/ceph/data/etc:/etc/ceph -v /docker/ceph/data/lib:/var/lib/ceph/ -e MON_IP=192.168.178.221 -e CEPH_PUBLIC_NETWORK=192.168.178.0/24 --ip=192.168.178.221 --network=macvlan0 --name ceph_mon2 ceph/daemon mon
docker run -d -v /docker/ceph/data/lib:/var/lib/ceph/ -v /docker/ceph/data/etc:/etc/ceph -e CEPHFS_CREATE=0 -e MDS_NAME=mds-$(hostname)-a --ip=192.168.178.245 --network=macvlan0 --name ceph_mds_a ceph/daemon mds

docker run -d -v /docker/ceph/data/etc:/etc/ceph -v /docker/ceph/data/lib:/var/lib/ceph/ -e MON_IP=192.168.178.222 -e CEPH_PUBLIC_NETWORK=192.168.178.0/24 --ip=192.168.178.222 --network=macvlan0 --name ceph_mon3 ceph/daemon mon
docker run -d -v /docker/ceph/data/lib:/var/lib/ceph/ -v /docker/ceph/data/etc:/etc/ceph -e CEPHFS_CREATE=0 -e MDS_NAME=mds-$(hostname)-b --ip=192.168.178.246 --network=macvlan0 --name ceph_mds_b ceph/daemon mds

exit 0
