from fetcher import fetch_json
from parser import parse_products_from_json

def scrape_collection(collection_url, limit=None):
    json_url = collection_url.rstrip("/") + "/products.json"

    json_data = fetch_json(json_url)

    if json_data is None:
        print("JSON endpoint not available")
        return []

    rows = parse_products_from_json(json_data, collection_url, limit)
    return rows