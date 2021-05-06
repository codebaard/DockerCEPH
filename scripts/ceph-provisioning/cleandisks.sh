#!/bin/bash

DEVPATH=/dev/disk/by-id/

#docker ps -a | grep ceph | xargs docker stop | xargs docker rm

#pvremove /dev/disk/by-id/dm-name-ceph--0d1801be--1eb4--4416--8aec--f21db2fcecbd-osd--block--a23b2748--a804--4cbb--bb18--633d6d2f1394
#dmsetup remove /dev/disk/by-id/dm-name-ceph--17bf8f13--d771--4500--96d4--81a1b1118328-osd--block--43188985--1194--4f1a--93bb--2b243e935319

ls $DEVPATH | grep dm-name | awk -v path="$DEVPATH" '{ print path$1 }' | xargs dmsetup remove
pvdisplay | grep VG | awk {'print $3'} | xargs vgremove -y
ls $DEVPATH | grep lvm | awk -v path="$DEVPATH" '{ print path$1 }' | xargs pvremove

sgdisk --zap-all /dev/sd{e,f,h,i,j,k1,k2,l,m}

exit 0

