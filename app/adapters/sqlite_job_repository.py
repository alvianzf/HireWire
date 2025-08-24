import sqlite3
from typing import List
from app.adapters.apify_linkedin_scraper import Job

class SQLiteJobRepository:
    def __init__(self, db_path="jobs.db"):
        self.conn = sqlite3.connect(db_path)
        self.init_schema()

    def init_schema(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            url TEXT PRIMARY KEY
        )
        """)
        self.conn.commit()

    def bulk_upsert(self, jobs: List[Job]):
        with self.conn:
            for job in jobs:
                self.conn.execute("""
                    INSERT OR REPLACE INTO jobs (title, company, location, description, url)
                    VALUES (?, ?, ?, ?, ?)
                """, (job.title, job.company, job.location, job.description, job.url))

    def list_all(self) -> List[Job]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT title, company, location, description, url FROM jobs")
        rows = cursor.fetchall()
        return [Job(*row) for row in rows]
