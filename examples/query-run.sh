#!/bin/bash
set -eu

# QUERY RUN
# Attempt to find run_id:1 .  Produces numFound="0"

wget -q -O - "http://localhost:8983/solr/run/select?q=run_id:*"
