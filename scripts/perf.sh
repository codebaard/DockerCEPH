#!/bin/bash

## db connection
dbuser=root
dbhost=127.0.0.1
dbpass=cmrep

## db test config
intcols=5
charcols=20

## iterations over concurrent users
user_min=4
user_max=20
iterations=3
samples=5

## queries per perfomance batch
total_queries=1024

for ((s=0; s<$samples; s++)) do
	echo "Starting Sample number: $s"

	for (( i=$user_min; i<=user_max; i++)) do
		
		queries_corrected=$((total_queries + (total_queries % $i)))
		mysqlslap --user=$dbuser --host=$dbhost  --password=$dbpass --concurrency=$i --iterations=$iterations --number-int-cols=$intcols --number-char-cols=$charcols --number-of-queries=$queries_corrected --auto-generate-sql -v

	done
done

exit 0