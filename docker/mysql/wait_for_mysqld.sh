#!/bin/bash

until mysqladmin ping -h mysql --silent; do
  echo 'waiting for mysqld...'
  sleep 3
done
