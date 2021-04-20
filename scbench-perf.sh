#!/bin/bash

ceph osd pool create scbench 128 128

rados bench -p scbench 10 write --no-cleanup
rados bench -p scbench 10 seq
rados bench -p scbench 10 rand
rados -p scbench cleanup

rados bench -p scbench 30 -t 32 write --no-cleanup
rados bench -p scbench 30 -t 32 seq
rados bench -p scbench 30 -t 32 rand
rados -p scbench cleanup

rados bench -p scbench 60 -t 64 write --no-cleanup
rados bench -p scbench 60 -t 64 seq
rados bench -p scbench 60 -t 64 rand
rados -p scbench cleanup

exit 0