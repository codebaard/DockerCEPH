#!/bin/bash

## db connection
dbuser=root
dbhost=localhost
dbpass=cmrep

## db test config
intcols=5
charcols=20

## iterations over concurrent users
user_min=4
user_max=20
iterations=5

## queries per perfomance batch
total_queries=2048

for (( i=$user_min; i<=user_max; i++))
	do

	queries_corrected=$((total_queries + (total_queries % $i)))
	mysqlslap --user=$dbuser -p$dbpass --host=$dbhost  --concurrency=$i --iterations=$iterations --number-int-cols=$intcols --number-char-cols=$charcols --number-of-queries=$queries_corrected --auto-generate-sql -v

	done

exit 0