#!/bin/bash
#  request URL passed as an argument
curl -sw '%{http_code}' -o /dev/null "$1"
