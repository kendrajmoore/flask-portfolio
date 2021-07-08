#!/bin/sh

number="200"
url=(https://kjmoore.duckdns.org, https://kjmoore.duckdns.org/register, https://kjmoore.duckdns.org/login, https://kjmoore.duckdns.org/kendra)

for i in ${url[@]}; do
    status="$(curl ${url[@]} -I -o headers -s)"
 
    response="$(cat headers | head -n 1 | cut '-d ' '-f2')"
    if [ "${response}" -eq ${number} ] ; then
        echo "0"
        curl -s -X POST "$1" -d "content=🚀 Deployment Successful"
    else
        echo "1"
        curl -s -X POST "$1" -d "content=😒 Deployment unsucessful"
    fi
done
