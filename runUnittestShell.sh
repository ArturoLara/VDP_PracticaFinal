#!/usr/bin/env bash



find . -name "tests*.py" -print | while read f; do
        echo "$f"
        ###
        python2 "$f"
        ###
done
