#!/bin/bash
set -eu

# INSERT RUN
# Trying to imitate https://cwiki.apache.org/confluence/display/solr/Uploading+Data+with+Index+Handlers

curl -X POST -H 'Content-Type: application/json' \
     'http://localhost:8983/solr/run/update/json/docs' --data-binary \
     $*
