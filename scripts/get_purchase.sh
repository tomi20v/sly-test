#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <purchase_id>"
  exit 1
fi

PURCHASE_ID=$1
curl http://localhost:5000/api/purchases/$PURCHASE_ID
