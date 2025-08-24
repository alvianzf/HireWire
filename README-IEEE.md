# LinkedIn Job Scraper

**Title:** Asynchronous LinkedIn Job Scraper Using Apify

**Authors:** Alvian Zachry Faturrahman, M.Si

**Affiliation:** Devshore Partners, s.r.o

---

## Abstract

This document presents the design and implementation of an asynchronous LinkedIn job scraper. The scraper collects job postings from LinkedIn based on user-specified queries and locations, stores them in a local SQLite database, and supports pagination for efficient data collection. The architecture follows hexagonal principles, separating scraping logic from storage to allow future integration with multi-agent AI systems.

---

## Keywords

LinkedIn scraping, asynchronous Python, Apify, SQLite, hexagonal architecture, job postings.

---

## 1. Introduction

Recruiters and HR professionals spend significant time monitoring job postings on LinkedIn. Automating this task can save effort and enable better candidate-job matching. This project implements a Python-based, asynchronous scraper that:

* Fetches LinkedIn job postings using the Apify platform.
* Supports keyword-based queries and location filtering.
* Stores job postings in SQLite for further analysis or matching.
* Provides a CLI interface for easy usage.

The design emphasizes modularity and future integration with multi-agent AI workflows.

---

## 2. System Architecture

### 2.1 Architecture Overview

The scraper is designed following **hexagonal architecture**, where core logic (domain) is decoupled from external services (adapters).

**ASCII Diagram:**

```
        +-----------------------+
        |       CLI Entry       |
        +-----------+-----------+
                    |
                    v
        +-----------------------+
        |   Container / Orches. |
        +-----------+-----------+
                    |
    +---------------+---------------+
    |                               |
+---v---+                       +---v---+
| Scraper |                     | Repository |
| (Apify) |                     | (SQLite)  |
+-------+                       +-----------+
                    |
                    v
             +--------------+
             | Job Objects  |
             +--------------+
```

* **CLI Entry:** User specifies queries, locations, max items, and output options.
* **Container / Orchestrator:** Instantiates and connects the scraper and repository.
* **Scraper (Adapter):** Uses Apify API asynchronously to fetch job postings with pagination.
* **Repository (Adapter):** Stores and retrieves job objects in SQLite.

---

## 3. Implementation

### 3.1 Technologies

* Python 3.13
* [Apify Python SDK](https://docs.apify.com/sdk/python) for LinkedIn scraping
* SQLite for persistent storage
* `asyncio` for asynchronous operations
* Pydantic for configuration and environment variable management

### 3.2 Data Model

Job postings are stored with the following fields:

| Field        | Type   | Description     |
| ------------ | ------ | --------------- |
| id           | int    | Primary key     |
| title        | string | Job title       |
| company      | string | Company name    |
| location     | string | Job location    |
| url          | string | Job posting URL |
| date\_posted | string | Posting date    |

### 3.3 CLI Usage

Example command:

```bash
python cli.py --queries "Python Developer,Data Engineer" --locations "Singapore,Jakarta" --max-items 10 --list
```

* `--queries` : comma-separated job titles.
* `--locations` : comma-separated job locations.
* `--max-items` : maximum number of job postings to fetch.
* `--list` : print fetched jobs to console.

---

## 4. Error Handling

* Missing or invalid Apify token raises a clear message and exits gracefully.
* Network or API errors are caught and logged.
* Pagination ensures that large queries do not overload the API.

---

## References

1. Apify SDK for Python. [https://docs.apify.com/sdk/python](https://docs.apify.com/sdk/python)
2. Pydantic Settings Documentation. [https://docs.pydantic.dev/2.11/migration/#basesettings-has-moved-to-pydantic-settings](https://docs.pydantic.dev/2.11/migration/#basesettings-has-moved-to-pydantic-settings)
3. SQLite Documentation. [https://www.sqlite.org/docs.html](https://www.sqlite.org/docs.html)
4. Python `asyncio` Documentation. [https://docs.python.org/3/library/asyncio.html](https://docs.python.org/3/library/asyncio.html)

---