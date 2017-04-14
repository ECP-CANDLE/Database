#!/usr/bin/env python

# RUN INSERT

from __future__ import print_function
import pysolr

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/run', timeout=10)

def run_insert(run_id, parameters):
    solr.add([
        {
            "run_id": run_id,
            "parameters": parameters,
        }])

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Requires: run_id parameters")
        sys.exit(1)
    run_id = sys.argv[1]
    parameters = sys.argv[2]
    run_insert(run_id, parameters)
