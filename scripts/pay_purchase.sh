#!/bin/bash
SCRIPT_DIR=$(dirname "$0")
cd "$SCRIPT_DIR/../backend" && ./pay_purchase.py "$1"
