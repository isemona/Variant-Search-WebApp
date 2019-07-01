# Variant Search Web Application

Variant Search Engine is a Flask backend and React frontend web application that allows users to search for genes and their respective variants and variant-attributes. 

## Features include:
1. A search field that allow users to enter a gene and returns a tabular view of each variant and their attributes.

2. Provides an auto-suggest feature for entering the gene name for faster lookup.

## Datasource
The data located in the variants.tsv file contains a sequence of genes and inter-genetic regions. For the purpose of this project the inter-genetic regions or blank spaces in the sequence have been removed. 

Excluding the intergentic regions (660 total) the file contains:
4345 Unique Genes
47855 Variants (rows)

## Install requirements

1. virtualenv -p python3 env
2. source env/bin/activate
3. pip install -r requirements.txt

## Run the backend and frontend separately

Flask-backend directory contains server.py <br />
$ cd /Flask-backend <br />
$ python3 server.py <br />

react-frontend directory contains index.html, App.js <br />
$ cd /frontend <br />
$ npm start <br />



