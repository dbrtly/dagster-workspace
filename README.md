# Dagster workspaces with multiple code locations.

Dagster includes a capability to include multiple components with conflicting package dependencies.

This workspace contains two packages: inventory and sales.

The two dagster packages have dependency differences.
- different version of Python
- different version of cowsay 

## How to

- install uv
https://docs.astral.sh/uv/getting-started/installation/#standalone-installer

```shell
chmod +x ./scripts/*
./scripts/demo_up.sh

```

open a new terminal and run:

```shell
./scripts/demo_materialize.sh
./scripts/demo_results.sh

```



## research about uv workspaces.

Dagster does not work with uv workspaces.

### experimental uv config for workspaces

https://github.com/astral-sh/uv/issues/6935
https://github.com/astral-sh/uv/issues/6874
https://github.com/DavidVujic/python-polylith-example-uv/blob/main/README.md
https://github.com/JuanoD/uv-mono/blob/main/README.md

```toml
[tool.uv]
package = false

[tool.uv.sources]
inventory = { workspace = true }
sales = { workspace = true }

[tool.uv.workspace]
members = ["packages/inventory", "packages/sales"]

```
