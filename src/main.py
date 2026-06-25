import argparse
from scraper import scrape_collection
from storage import save_csv

def parse_args():
    parser = argparse.ArgumentParser(
        description="Export products from a Shopify collection to CSV."
    )

    parser.add_argument("collection_url")
    parser.add_argument("output_file")
    parser.add_argument("--limit", type=int, default=None)

    return parser.parse_args()


def main():
    args = parse_args()

    rows = scrape_collection(args.collection_url, args.limit)

    print(f"Total products parsed: {len(rows)}")

    save_csv(args.output_file, rows)


if __name__ == "__main__":
    main()