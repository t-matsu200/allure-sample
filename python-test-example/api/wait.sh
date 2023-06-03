#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

echo 'Waiting for mysql'
until mysqladmin ping -h "$host" --silent; do
  echo 'Waiting for mysqld to be connectable...'
  sleep 2
done

exec $cmd
