#!/usr/bin/env python

# RUN INSERT

from __future__ import print_function
import pysolr

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/run', timeout=10)

def run_insert(run_id, parameters,
               benchmark_id  = "unknown",
               dataset_id    = "unknown",
               experiment_id = "unknown",
               start_time    = None,
               end_time      = None,
               runtime_hours = None,
               status        = "SUCCESS",
               run_progress  = None,
               training_accuracy = None,
               training_loss = None,
               validation_accuracy = None,
               validation_loss = None,
               model_checkpoint_file = None,
               model_description_file = None,
               model_weight_file = None,
               model_result_files = None):
    solr.add([
        {
            "run_id": run_id,
            "parameters": parameters,
            "benchmark_id": benchmark_id

        }])

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Requires: run_id parameters")
        sys.exit(1)
    run_id = sys.argv[1]
    parameters = sys.argv[2]
    run_insert(run_id, parameters)
