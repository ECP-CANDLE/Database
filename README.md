# Database

## Setup

1. Download Solr TGZ:
```
wget http://archive.apache.org/dist/lucene/solr/6.5.0/solr-6.5.0.tgz
tar xfz solr-6.5.0.tgz
```

2. Add .../solr-6.5.0/bin to PATH

3. Checkout the Database schemas
```
git clone git@github.com:ECP-CANDLE/Database.git
```

4. Start solr as yourself with these schemas
You can specify solr home directory by using -Dsolr.solr.home param
```
./bin/solr start -Dsolr.solr.home=.../Database
```
All data is stored in .../Database

5. Start inserting data with the examples in Database/examples

## Basic operation reference

### Command line tools

* A `curl`-based insertion is [here](https://github.com/ECP-CANDLE/Database/blob/master/examples/run-insert.sh)
* A `wget`-based query is [here](https://github.com/ECP-CANDLE/Database/blob/master/examples/run-query.sh)

### Python

We are using [pysolr](https://pypi.python.org/pypi/pysolr/3.4.0) to access the database from workflows.

* A sample insertion is [here](https://github.com/ECP-CANDLE/Database/blob/master/examples/run-insert-py.sh)
* A sample query is ...
* Our WIP pysolr abstraction is [run_insert.py](https://github.com/ECP-CANDLE/Database/blob/master/py/run_insert.py)
[README](https://github.com/ECP-CANDLE/Database/tree/master/py)

## Workflow access
