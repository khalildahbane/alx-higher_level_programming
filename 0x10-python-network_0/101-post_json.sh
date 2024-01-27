#!/bin/bash
# sends a JSON POST request to a URL
responde=$(curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1")
