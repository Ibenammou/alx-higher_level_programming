#!/bin/bash
# script to send request to a URL and display size of the body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
