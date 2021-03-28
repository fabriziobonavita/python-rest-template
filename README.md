# Template for python rest services

This repository is serving as a template to base python rest webservices on
The scope of this service example covers:
* Fastapi uvicorn service
* SqlAlchemy setup
* Nox sessions for tests, linting, type checking, formatting and docs
* Dependency management with poetry

## Setup

Setup and run simply by

    git clone git@github.com:fabriziobonavita/python-rest-template.git
    poetry install
    .venv/bin/uvicorn src.project_name.main:app --reload

Run all available nox sessions
    
    nox
    
List all available nox sessions

    nox --list

## TODOS
* Fix warnings
* Setup alembic properly

