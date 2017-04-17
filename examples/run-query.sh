#!/bin/bash
set -eu

# RUN QUERY
# For run_id

# wget -q -O - "http://localhost:8983/solr/run/select?q=run_id:*"

# Request JSON output:
wget -q -O - "http://localhost:8983/solr/run/select?q=run_id:*&wt=json"
