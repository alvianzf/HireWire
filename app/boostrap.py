from apify_client import ApifyClient
from app.infrastructure.settings import Settings
from app.adapters.apify_linkedin_scraper import ApifyLinkedInJobsScraper
from app.adapters.sqlite_job_repository import SQLiteJobRepository
from app.domain.use_cases import ScrapeAndStoreJobs

class Container:
    def __init__(self):
        self.settings = Settings.load()
        self.apify_client = ApifyClient(self.settings.apify_token)
        self.scraper = ApifyLinkedInJobsScraper(self.apify_client)
        self.repository = SQLiteJobRepository()
        self.scrape_and_store = ScrapeAndStoreJobs(scraper=self.scraper, repository=self.repository)
