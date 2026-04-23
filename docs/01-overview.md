# Project Overview

## Project name
Event-Driven Data Pipeline and Monitoring System

## Purpose
This project demonstrates a small pipeline service that can:
- trigger a data pull from an external source
- transform the resulting items
- track pipeline run status
- expose run history through a REST API

## What problem it solves
Operational data pipelines need a simple way to record run status, processed counts, and retry/failure information. This project focuses on that monitoring pattern.

## Core capabilities
- event-driven pipeline trigger via API
- data fetch from an external HTTP source
- basic transformation logic
- persistence of run metadata
- retrieval of pipeline run history
- starter Airflow DAG for scheduling

## Primary technology stack
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL-oriented schema design
- Docker
- Airflow starter DAG

## Target use
This repository is suited for:
- portfolio demonstration
- backend data pipeline demo
- starter monitoring service for pipeline workflows
