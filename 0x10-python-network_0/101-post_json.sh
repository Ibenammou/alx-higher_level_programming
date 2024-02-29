#!/bin/bash
# script to send a JSON POST request to a URL with the contents
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
