#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE IF NOT EXISTS weather_table(city TEXT,country TEXT,latitude REAL,longitude REAL,todays_date DATE,humidity REAL,pressure REAL,min_temp REAL,max_temp REAL,temp REAL,weather TEXT);
EOSQL