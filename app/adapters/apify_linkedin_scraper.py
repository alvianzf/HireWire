from typing import List
from apify_client import ApifyClient
import asyncio
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

@dataclass
class Job:
    title: str
    company: str | None
    location: str | None
    description: str | None
    url: str | None

def clean_text(text: str | None) -> str | None:
    return text.strip() if text else text

class ApifyLinkedInJobsScraper:
    def __init__(self, client: ApifyClient, actor_id: str = "apify/linkedin-jobs-scraper"):
        self.client = client
        self.actor_id = actor_id
        self.executor = ThreadPoolExecutor(max_workers=4)

    async def fetch_jobs(self, queries: List[str], locations: List[str], max_items: int = 10, page_size: int = 5):
        jobs_collected = []
        total_pages = (max_items + page_size - 1) // page_size

        for page in range(total_pages):
            run_input = {
                "queries": queries,
                "locations": locations,
                "maxItems": page_size,
                "offset": page * page_size
            }

            run = await asyncio.get_event_loop().run_in_executor(
                self.executor,
                lambda: self.client.actor(self.actor_id).call(run_input=run_input)
            )

            dataset_id = run["defaultDatasetId"]

            items = await asyncio.get_event_loop().run_in_executor(
                self.executor,
                lambda: list(self.client.dataset(dataset_id).iterate_items())
            )

            for item in items:
                job = Job(
                    title=clean_text(item.get("title")),
                    company=clean_text(item.get("companyName")),
                    location=clean_text(item.get("location")),
                    description=clean_text(item.get("description")),
                    url=clean_text(item.get("url")),
                )
                jobs_collected.append(job)

            if len(jobs_collected) >= max_items:
                break

        return jobs_collected[:max_items]
