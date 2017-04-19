#!/bin/bash
set -eu

# INSERT RUN
# Trying to imitate https://cwiki.apache.org/confluence/display/solr/Uploading+Data+with+Index+Handlers

if [[ ${#} == 0 ]]
then
  echo "Requires JSON input!"
  exit 1
fi

curl -H 'Content-Type: application/json' \
     'http://localhost:8983/solr/run/update/json/docs?commit=true' --data-ascii \
     $*
