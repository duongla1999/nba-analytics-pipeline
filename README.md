# NBA Analytics Pipeline

A small end-to-end data engineering pipeline built to practice the core DE toolkit - Python, SQL, dbt and Power Bi using real NBA data.

## Overview

This project ingests NBA game and team data from a public kaggle dataset, loads it into local PostgreSQL warehouse and transform it into analytic-ready star schema for dashboarding.

## Tech Stack

| Layer | Tool |
|---|---|
| Ingestion | Python, pandas |
| Loading | SQLAlchemy, psycopg2 |
| Warehouse | PostgreSQL 16 (Docker) |
| Dependency management | uv |
| Transformation (in progress) | dbt-postgres |
| Visualization (planned) | Power BI |

## Data Source


[`eoinamoore/historical-nba-data-and-player-box-scores`](https://www.kaggle.com/datasets/eoinamoore/historical-nba-data-and-player-box-scores) — historical NBA box scores from 1947 to present, updated nightly.

For this project, data is scoped down to the **2025–2026 regular season** to keep the pipeline lightweight while covering the full toolset.

## Getting Started

**Prerequisites:** Docker Desktop, a free [Kaggle](https://www.kaggle.com/) account (for the dataset), Python with [uv](https://github.com/astral-sh/uv).

```bash
# 1. Clone the repo
git clone https://github.com/duongla1999/nba-analytics-pipeline.git
cd nba-analytics-pipeline

# 2. Copy .env.example to .env and fill in your own Postgres credentials
cp .env.example .env

# 3. Start Postgres
docker compose up -d

# 4. Create the raw schema
docker exec -it nba_postgres psql -U <user> -d <db> -c "CREATE SCHEMA IF NOT EXISTS raw;"

# 5. Install dependencies
uv sync

# 6. Download the dataset from Kaggle into ./data, then run the pipeline
uv run main.py
```

## Data Scope

- Filtered to `gameType = 'Regular Season'`, games between `2025-10-01` and `2026-06-30`.
- Loaded into schema `raw`: `games`, `players`, `teamStatistics`, `teamHistories`.
- Intentionally excluded for this MVP: `PlayerStatistics` (~400MB) and `PlayByPlay` (~900MB) — large, detailed tables not needed for the current scope; may be added later.

## Project Status

- [x] **Week 1** — Environment setup, Postgres via Docker, CSV ingestion into `raw` schema, data quality checks (row counts, key uniqueness, date range, NULL checks).
- [ ] **Week 2** — dbt staging models and a Kimball star schema in a `marts` schema, with dbt tests and docs.
- [ ] **Week 3** — Power BI dashboard on top of `marts`.
