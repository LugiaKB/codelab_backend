#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pipenv install --deploy --ignore-pipfile

# Apply any outstanding database migrations
pipenv run python manage.py migrate