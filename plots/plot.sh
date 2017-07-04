#!/bin/bash
set -eu

if [[ ${#*} != 1 ]]
then
  echo "Provide MODE!"
  exit 1
fi
MODE=$1

# JWPLOT: https://github.com/jmjwozniak/jwplot
jwplot $MODE.{cfg,eps,data}
# convert $MODE.{eps,pdf}
