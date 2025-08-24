# LinkedIn Job Scraper

[![Python](https://img.shields.io/badge/python-3.13-blue?logo=python)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Apify](https://img.shields.io/badge/Apify-LinkedIn%20Scraper-orange)](https://apify.com/)  
[![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)](https://www.sqlite.org/docs.html)  

**Version:** 1.0.0  
**Last Updated:** 24 August 2025  
**Author:** Alvian Zachry Faturrahman 

---

## Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Technology Stack](#technology-stack)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Architecture](#architecture)  
7. [Data Model](#data-model)  
8. [Error Handling](#error-handling)  
9. [License](#license)  

---

## Overview
The LinkedIn Job Scraper is an **asynchronous Python CLI application** that automates the extraction of LinkedIn job postings based on user queries and locations. It stores results in an SQLite database and supports pagination, making it scalable and maintainable. The scraper is designed to integrate with multi-agent AI systems for future candidate-job matching workflows.

---

## Features
- Scrape LinkedIn job postings using **Apify**.  
- Supports **keyword queries** and **location filters**.  
- Stores job postings in **SQLite** database.  
- **Asynchronous** scraping for faster execution.  
- CLI interface for easy execution and listing of jobs.  
- Pagination support to handle large result sets.  
- Clear error handling for missing API tokens or network errors.

---

## Technology Stack
| Component             | Technology / Library |
|-----------------------|-------------------|
| Programming Language  | Python 3.13        |
| Async Framework       | asyncio            |
| Web Scraper API       | Apify Python SDK   |
| Database              | SQLite             |
| Configuration         | pydantic-settings, python-dotenv |
| Package Management    | pip, venv          |

---

## Installation
1. Clone the repository:

```bash
git clone https://github.com/username/linkedIn-job-scraper.git
cd linkedIn-job-scraper
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Apify token:

```
APIFY_TOKEN=your_real_token_here
```

---

## Usage

Run the CLI to scrape jobs:

```bash
python cli.py --queries "Python Developer,Data Engineer" --locations "Singapore,Jakarta" --max-items 10 --list
```

**Arguments:**

* `--queries` : Comma-separated job titles.
* `--locations` : Comma-separated locations.
* `--max-items` : Maximum number of jobs to fetch.
* `--list` : List jobs in console after scraping.

---

## Architecture

The project follows a **hexagonal architecture**:

```
        +-----------------------+
        |       CLI Entry       |
        +-----------+-----------+
                    |
                    v
        +----------------------------+
        | Container / Orchestrator  |
        +-----------+----------------+
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

* **CLI Entry:** Accepts user queries and locations.
* **Container / Orchestrator:** Initializes scraper and repository.
* **Scraper:** Async calls to Apify API with pagination.
* **Repository:** Stores jobs in SQLite database.

---

## Data Model

| Field        | Type | Description     |
| ------------ | ---- | --------------- |
| id           | int  | Primary key     |
| title        | str  | Job title       |
| company      | str  | Company name    |
| location     | str  | Job location    |
| url          | str  | Job posting URL |
| date\_posted | str  | Posting date    |

---

## Error Handling

* **Missing API Token:** Exits gracefully with a clear message.
* **Network / API Errors:** Logged with retry support if necessary.
* **Pagination:** Ensures large queries do not overload API.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.