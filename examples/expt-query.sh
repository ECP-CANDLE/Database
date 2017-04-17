#!/bin/bash
set -eu

# EXPT QUERY
# For experiment_id

# Request JSON output:
wget -q -O - "http://localhost:8983/solr/run/select?q=experiment_id:*&wt=json"
