#!/bin/bash
# script takes in a URL sends a POST request
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
