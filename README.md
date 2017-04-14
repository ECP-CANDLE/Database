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

## Workflow access
