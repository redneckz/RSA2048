#!/usr/bin/env bash

HOST=localhost
PORT=8786
NTHREADS=16
MEM_LIMIT='1G'

source ./env/bin/activate

dask worker "${HOST}":"${PORT}"  --nworkers auto --nthreads "${NTHREADS}" --memory-limit "${MEM_LIMIT}" --name "$1"
