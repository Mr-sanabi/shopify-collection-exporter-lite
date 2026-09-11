# Shopify Collection Exporter Lite

A Python 3.11+ CLI that exports public Shopify collections to CSV, with one row per product variant.

## Run

Replace the example URL with a public collection you are allowed to access.

```bash
python -m pip install -r requirements.txt
python src/main.py data/products.csv --collection-url "https://store.example/collections/shoes" --limit 25
```

Use `--collections-file data/collections.txt` instead of `--collection-url` for one collection URL per line. `--limit` counts products per collection, not variant rows.

CSV includes product details, variant options, price, SKU, first image, availability, source collection, and extraction time.

## Limits

One `products.json` request per collection: no pagination or deduplication across collections. Not Shopify's import CSV format. Failed collections may leave a partial dataset; respect access restrictions and rate limits.

## Tests

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
