#!/usr/bin/env bash



find . -name "tests*.py" -print | while read f; do
        echo "$f"
        ###
        python "$f"
        ###
cd /var/lib/jenkins/workspace/test
python manage.py runserver 0.0.0.0:8000
done
