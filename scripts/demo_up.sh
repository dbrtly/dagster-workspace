#!/bin/bash

# sets up Python virtual environments with libraries 
# and starts dagster webserver

root=$PWD

uv sync
cd packages/inventory && uv sync
cd "${root}"

cd packages/inventory && uv sync
cd "${root}"

# according to the documentation, these commands should have identical functionality
# https://docs.dagster.io/_apidocs/cli#dagster-webserver
# see examples 1 and 2

uv run dagster dev 
uv run dagster dev --workspace workspace.yaml
