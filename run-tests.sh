#!/usr/bin/env bash

set -x
echo "Run pytests for unit-tests"
pytest
echo "Run pytest for syntax (flake8)"
pytest --flake8
