# Shopify Collection Exporter Lite

A Python CLI tool that exports product data from a selected Shopify collection/category into a clean CSV file.

This project focuses on a common e-commerce workflow: instead of exporting an entire Shopify store, the tool extracts products from a specific collection URL and saves structured product data that can be reviewed, cleaned, or prepared for Shopify import.

## Features

* Accepts a Shopify collection/category URL
* Uses Shopify’s public `products.json` endpoint when available
* Extracts product data from a selected collection
* Supports an optional `--limit` argument
* Exports structured product data to CSV
* Includes product title, URL, price, images, variants, SKU, and availability fields
* Adds scrape timestamp for later comparison
* Handles unavailable JSON endpoints without crashing
* Works as a simple command-line tool

## Why This Project

Many Shopify product export tools export the entire store. In real workflows, the user often needs only selected categories or collections, such as:

* Sale items
* Clearance products
* Men’s clothing
* Women’s shoes
* Specific product categories

This tool is designed as a lightweight first version for exporting products from selected Shopify collections into CSV.

## Tech Stack

* Python
* requests
* csv
* argparse
* datetime
* urllib.parse

## Project Structure

```text
shopify-collection-exporter-lite/
  src/
    main.py
    fetcher.py
    parser.py
    scraper.py
    storage.py
    logger_config.py

  data/
    .gitkeep

  README.md
  requirements.txt
  .gitignore
```

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the tool:

```bash
python src/main.py <collection_url> <output_file> --limit <number>
```

Example:

```bash
python src/main.py https://www.allbirds.com/collections/mens data/products.csv --limit 5
```

The `--limit` argument is optional.

Example without limit:

```bash
python src/main.py https://www.allbirds.com/collections/mens data/products.csv
```

## Output Fields

The CSV includes the following columns:

```text
product_title
product_url
description
price
compare_at_price
variant_title
sku
image_url
availability
source_collection
scraped_at
```

## Example Output

```csv
product_title,product_url,description,price,compare_at_price,variant_title,sku,image_url,availability,source_collection,scraped_at
Men's Tree Runner NZ - Natural White,https://www.allbirds.com/products/mens-tree-runner-nz-natural-white,,100.00,,8,A11914M8B,https://cdn.shopify.com/...,True,https://www.allbirds.com/collections/mens,2026-06-25T10:23:06
```

## Notes

Some fields may be empty depending on what the Shopify store exposes through its public product data.

For example:

* `description` may be empty if the store does not expose `body_html`
* `sku` may be empty if product variants do not include SKU values
* `compare_at_price` may be empty if the item is not discounted
* `availability` depends on the data exposed by the store

## Current Limitations

This is a lightweight MVP version.

It currently:

* Uses the public Shopify JSON endpoint
* Extracts the first product variant
* Extracts the first product image
* Does not yet export all variants as separate rows
* Does not include advanced inventory monitoring
* Does not bypass anti-bot systems or login-protected stores

## Possible Improvements

Future versions could include:

* Exporting all product variants as separate rows
* Better Shopify import CSV formatting
* Inventory comparison between multiple exports
* Support for multiple stores and collection URLs
* HTML fallback if `products.json` is unavailable
* Product handle-based change tracking
* Cleaner formatting for descriptions

## What I Practiced

* Building a Shopify-specific data extraction workflow
* Working with public JSON endpoints
* Parsing nested product, image, and variant data
* Building product URLs from Shopify handles
* Exporting structured CSV files
* Adding optional CLI arguments with `argparse`
* Handling missing fields safely
* Structuring a Python project into clean modules

## Compliance Note

This tool is intended for extracting publicly available product data from accessible Shopify collection pages.

It does not bypass logins, captchas, private APIs, or restricted access systems. Use it only on websites where automated access is allowed and always respect each website’s terms of service and robots.txt.
