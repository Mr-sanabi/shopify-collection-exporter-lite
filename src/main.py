import argparse
from scraper import scrape_collection
from storage import save_csv

def positive_int(value):
    try:
        val =  int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Limit must be a value")
    
    if val <= 0:
        raise argparse.ArgumentTypeError("Limit must be a positive integer")
    else:
        return val
def parse_args():
    parser = argparse.ArgumentParser(
        description="Export products from a Shopify collection to CSV."
    )
    source_group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument("output_file")
    source_group.add_argument("--collection-url")
    source_group.add_argument("--collections-file")
    parser.add_argument("--limit", type=positive_int, default=None)

    return parser.parse_args()

def load_collection_urls(input_file):
    rows = []
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                clean_url = line.strip()

                if not clean_url:
                    continue
                    
                rows.append(clean_url)
            
            return rows
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return []


def main():
    args = parse_args()

    if args.collections_file:
        collection_urls = load_collection_urls(args.collections_file)
    
    elif args.collection_url:
        collection_urls =  [args.collection_url]

    else:
        print("Please provide --colection-url or --collections-file")
        return

    all_rows = []
    for collection_url in collection_urls:
        rows = scrape_collection(collection_url, args.limit)
        all_rows.extend(rows)
    

    print(f"Total products parsed: {len(all_rows)}")

    save_csv(args.output_file, all_rows)


if __name__ == "__main__":
    main()