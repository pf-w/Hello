#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: bash bootstrap.sh LOG_LEVEL"
    echo "LOG_LEVEL=$1"
    exit 1
fi

LOG_LEVEL=$1
echo "LOG_LEVEL=$1"

python3 run.py --port=12000 --log_level=${LOG_LEVEL} --log_dir=/steamos/log
