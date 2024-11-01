# Dagster workspaces with multiple code locations.

Dagster includes a capability to include multiple components with conflicting package dependencies.




## experimental uv config for workspaces

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
