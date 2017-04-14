#!/bin/bash
set -eu
export SHELLOPTS

# RUN INSERT with PY
# Example usage of Python run insertion API

THIS=$( dirname $0 )
DATABASE_PY=$( set -e ; cd $THIS/../py ; /bin/pwd )
export PYTHONPATH=$PYTHONPATH:$DATABASE_PY

python $THIS/run-insert-example.py
