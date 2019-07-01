# Variant Search WebApp Installation

Variant Search Engine is a Flask backend and React frontend web application that allows users to search for genes and their respective variants and their attributes. 

## Features Include:
1. A search field that allow users to enter a gene and returns a tabular view of each variant and their attributes.

2. Provides an auto-suggest feature for entering the gene name for faster lookup.

## Datasource
Data contains gene names and intergenetic regions. For the purpose of this project the inter-genetic regions or blank spaces in the sequence have been removed. 

Without the intergentic regions (660 total) the file contains:
4345 Gene
47855 Variants (rows)

## Install requirements

1. virtualenv -p python3 env
2. source env/bin/activate
3. pip install -r requirements.txt

## Run the backend and frontend separately

Flask-backend directory contains server.py 
$ cd /Flask-backend
$ python3 server.py

react-frontend directory contains indext.html, App.js
$ cd /frontend
$ npm start




