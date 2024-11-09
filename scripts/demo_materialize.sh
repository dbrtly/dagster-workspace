#!/bin/bash

# Materialize assets in both code locations

root=$PWD

packages=(
    inventory,
    sales
)

for package in "${packages[@]}"; do
    while IFS= read -r asset; do
        assets+=("$asset")
    done < <(uv run dagster asset list --package-name "packages.${package}.src.${package}.definitions")
    for asset in "${assets[@]}"; do
        uv run dagster asset materialize \
            --package-name "packages.${package}.src.${package}.definitions" \
            --select "${asset}"
    done
done

for 