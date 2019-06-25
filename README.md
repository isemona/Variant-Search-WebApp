# Variant Search WebApp Installation

## Install requirements

1. virtualenv -p python3 env
2. source env/bin/activate
3. pip install -r requirements.txt

## Start the database
docker run --name postgres -e POSTGRES_PASSWORD= -p 5432:5432 -d postgres

## Create the database and seed the tables with default data.
python3 model.py
python3 seed.py

## Now, run the app
python3 server.py

