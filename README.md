# iGaming Clickstream Data Simulation & Analytics Pipeline

##  Overview

I’m building this project to simulate and analyze real-time player behavior for an iGaming platform. The goal is to replicate how online casinos generate clickstream data so I can explore how it flows through a modern data stack—from raw ingestion to actionable insights.

This is still a work in progress, but it already covers a lot of ground: a FastAPI-based generator, realistic event simulation using `mimesis`, auto-saving to timestamped CSVs, and a modular structure that makes it easy to extend. I plan to evolve this into a full-fledged streaming and analytics pipeline with PostgreSQL, dbt, and eventually Kafka + Spark.

---

## What I'm Solving

In the iGaming space, companies often struggle with:
- Fragmented or messy clickstream data
- Delayed access to player behavior insights
- Limited tooling around responsible gaming and anomaly detection

This project gives me a sandbox where I can:
- Simulate realistic betting and gameplay patterns
- Build clean pipelines that turn raw events into analysis-ready tables
- Create dashboards that support operational monitoring, customer support, and ethical gameplay alerts

---

## Real-World Use Cases

Some examples of what this pipeline is designed to support:
- How many players from Estonia played poker last night?
- Which players are betting large amounts unusually often?
- Are there any patterns that could suggest problem gambling or fraud?
- What are the most popular games, devices, or countries over time?

---

## Tech Stack

| Layer         | Tools I'm Using                |
|---------------|--------------------------------|
| Simulation    | FastAPI, Mimesis               |
| Storage       | PostgreSQL (coming soon)       |
| Transformation| dbt (planned)                  |
| Stream (next) | Kafka, Spark (planned)         |
| Visualization | Looker, Metabase, or Grafana   |
| Automation    | Airflow (future)               |

---

## Project Structure

```bash
igaming-data-pipeline/
│
├── app/                         # FastAPI app + generator logic
│   ├── main.py                  # Exposes /generate endpoint
│   ├── generator.py             # Generates clickstream events
│   └── config.py                # Config settings
│
├── generated_clickstreams/     # Auto-saved CSVs
│
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg_clickstream.sql
│   │   └── marts/
│   │       └── fct_player_metrics.sql
│   └── schema.yml
│
├── notebooks/                  # For exploration and plotting
│   └── clickstream_eda.ipynb
│
├── sql/                        # DDLs or manual SQL
│   └── create_raw_table.sql
│
├── .env
├── requirements.txt
└── README.md
````

---

## What’s Working Right Now

* `/generate` API endpoint that outputs synthetic player events to CSV
* Uses `mimesis` to randomize game name, event type, device, country, and betting behavior
* Every call creates a new CSV in `generated_clickstreams/`
* Designed to be modular and easy to scale

---

## What’s Coming Next

* [ ] Write clickstream events to PostgreSQL instead of just CSV
* [ ] Set up dbt staging + marts for clean analytics tables
* [ ] Build dashboards using Grafana or Metabase
* [ ] Add Kafka + Spark for real-time ingestion and processing
* [ ] Add responsible gaming alerts (e.g. 50+ sessions in a day)
* [ ] Schedule automated jobs with Airflow

---

## How I Use It

To test things locally, I just run:

```bash
uvicorn app.main:app --reload
```

Then I hit the API like this:

```
http://localhost:8000/generate?records=500
```

That generates 500 synthetic player activity events and stores them in a new CSV with a timestamped filename. I can then ingest it into PostgreSQL or explore it in a notebook.

---

## Contributions

This is a personal project, but I’d love to collaborate with anyone interested in data simulation, behavioral analytics, or building ethical, data-driven systems in iGaming or similar industries.


