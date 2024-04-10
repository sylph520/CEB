#!/bin/sh

createdb -U $POSTGRES_USER imdb

wget -O /var/lib/postgresql/pg_imdb.tar http://139.224.245.160:8084/d/public/aliyun_share_folder/pg_imdb.tar.gz
tar xf /var/lib/postgresql/pg_imdb.tar -C /var/lib/postgresql/
#psql -d imdb -U $POSTGRES_USER -c "SHOW max_wal_size";
pg_restore -v -d imdb -U $POSTGRES_USER /var/lib/postgresql/pg_imdb
