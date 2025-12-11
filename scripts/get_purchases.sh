#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <user_id>"
  exit 1
fi

USER_ID=$1
curl http://localhost:5000/api/user/$USER_ID/purchases
