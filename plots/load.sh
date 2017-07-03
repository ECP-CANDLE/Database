#!/bin/bash
set -e

# JWPLOT: https://github.com/jmjwozniak/jwplot
jwplot load.{cfg,eps,data}
convert load.{eps,pdf}
