#!/bin/bash
# script to take URL and display all HTTP mthods
curl -sI "$1" | grep -i Allow | cut -d " " -f 2-
