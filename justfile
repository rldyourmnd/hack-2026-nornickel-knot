set shell := ["bash", "-euo", "pipefail", "-c"]

# Lists the source-maintenance commands.
default:
    @just --list

# Installs the same frozen dependency set used by CI.
setup:
    uv sync --frozen

# Checks source and lock consistency without a network, model execution or bytecode files.
check:
    just --fmt --check
    uv lock --check --offline
    uv run --no-project --offline python -B tools/check_syntax.py

# Runs all source checks after the declared setup.
verify: check
