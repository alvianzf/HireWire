# Job_Scraper

### Project Structure
```bash
job_scraper/
├─ requirements.txt
├─ .env                      # APIFY_TOKEN=...
└─ app/
   ├─ main.py                # CLI entrypoint
   ├─ bootstrap.py           # wiring
   ├─ domain/
   │  ├─ entities.py         # Job entity
   │  ├─ ports.py            # interfaces
   │  └─ use_cases.py        # application services
   ├─ adapters/
   │  ├─ apify_linkedin_scraper.py  # outbound adapter
   │  ├─ sqlite_job_repository.py   # outbound adapter
   │  └─ text_normalizer.py         # cleaning utils
   └─ infrastructure/
      ├─ db.py               # SQLite connection
      └─ settings.py         # .env loader
```

