from typing import List
from app.adapters.apify_linkedin_scraper import Job

class ScrapeAndStoreJobs:
    def __init__(self, scraper, repository):
        self.scraper = scraper
        self.repository = repository

    async def execute(self, queries: List[str], locations: List[str], max_items: int = 10, page_size: int = 10):
        jobs = await self.scraper.fetch_jobs(queries, locations, max_items=max_items, page_size=page_size)
        self.repository.bulk_upsert(jobs)
        return len(jobs)
