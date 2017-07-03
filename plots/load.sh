#!/bin/bash
set -e

jwplot load.{cfg,eps,data}
convert load.{eps,pdf}
