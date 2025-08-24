import argparse
import asyncio
from app.bootstrap import Container

def parse_args():
    parser = argparse.ArgumentParser(description="LinkedIn Jobs scraper via Apify")
    parser.add_argument("--queries", type=str, required=True, help="Comma separated keywords")
    parser.add_argument("--locations", type=str, required=True, help="Comma separated locations")
    parser.add_argument("--max-items", type=int, default=10, help="Max items to fetch")
    parser.add_argument("--page-size", type=int, default=5, help="Items per page")
    parser.add_argument("--list", action="store_true", help="List all jobs after scraping")
    return parser.parse_args()

async def main_async():
    args = parse_args()
    queries = [q.strip() for q in args.queries.split(",") if q.strip()]
    locations = [l.strip() for l in args.locations.split(",") if l.strip()]

    c = Container()
    count = await c.scrape_and_store.execute(
        queries=queries,
        locations=locations,
        max_items=args.max_items,
        page_size=args.page_size
    )

    print(f"Stored {count} jobs.")
    if args.list:
        for j in c.repository.list_all():
            print(f"- {j.title} | {j.company} | {j.location} | {j.url}")

if __name__ == "__main__":
    asyncio.run(main_async())
