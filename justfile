VERSION := "0.0.2"
set shell := ["bash", "-c"]

build:
    docker compose build

start:
    docker compose up -d
    @echo "Project version: {{VERSION}}"

run-tests:
    @echo "Tests are running..."
    docker compose run --rm --entrypoint "bash -c 'pytest tests/'" backend