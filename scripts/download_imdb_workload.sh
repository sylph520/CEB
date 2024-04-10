#!/bin/sh

mkdir -p queries


## full CEB-IMDB workload
wget -O imdb.tar.gz http://139.224.245.160:8084/d/public/aliyun_share_folder/imdb.tar.gz
tar -xvf imdb.tar.gz
mv imdb queries/ceb-imdb-full
rm imdb.tar.gz

## downloading data about imdb schema etc.
wget -O imdb_data.json http://139.224.245.160:8084/d/public/aliyun_share_folder/imdb_data.json
cp imdb_data.json queries/ceb-imdb-full/dbdata.json

## CEB-IMDb UniquePlans workload (~3k queries, subset of full CEB-IMDb)
wget -O imdb-unique-plans.tar.gz http://139.224.245.160:8084/d/public/aliyun_share_folder/imdb-unique-plans.tar.gz

tar -xvf imdb-unique-plans.tar.gz
mkdir -p queries
mv imdb-unique-plans queries/ceb-imdb
rm imdb-unique-plans.tar.gz
cp imdb_data.json queries/ceb-imdb/dbdata.json

## JOB workload
wget -O job.tar.gz http://139.224.245.160:8084/d/public/aliyun_share_folder/job.tar.gz

tar -xvf job.tar.gz
mv job queries/
rm job.tar.gz
cp imdb_data.json queries/job/dbdata.json

# JOBLight_train
wget -O joblight_train.tar.gz http://139.224.245.160:8084/d/public/aliyun_share_folder/joblight_train.tar.gz

tar -xvf joblight_train.tar.gz
mv joblight_train queries/
rm joblight_train.tar.gz
cp imdb_data.json queries/joblight_train/dbdata.json

## JOB-M
wget -O jobm.tar.gz http://139.224.245.160:8084/d/public/aliyun_share_folder/jobm.tar.gz

mkdir -p queries
tar -xvf jobm.tar.gz
mv jobm queries/
rm jobm.tar.gz
cp imdb_data.json queries/jobm/dbdata.json

## download bitmaps for all these workloads
wget -O allbitmaps.tar.gz http://139.224.245.160:8084/d/public/aliyun_share_folder/allbitmaps.tar.gz
tar -xvf allbitmaps.tar.gz

mv allbitmaps queries/
rm allbitmaps.tar.gz

