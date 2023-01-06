VERSION := "0.0.2"
set windows-powershell := true 

build:
    docker compose build

start:
    docker compose up -d
    @echo "Project version: {{VERSION}}"

run-tests:
    @echo "Tests are running..."