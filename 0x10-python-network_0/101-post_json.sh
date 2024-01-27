#!/bin/bash
# sends a JSON POST request to a URl
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
