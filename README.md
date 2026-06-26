# Shopify Collection Exporter Lite

A Python CLI tool that exports product data from selected Shopify collections/categories into a clean CSV file.

This project focuses on a common e-commerce workflow: instead of exporting an entire Shopify store, the tool can extract products from one selected collection or from multiple selected collection URLs listed in a `.txt` file. The exported data can be reviewed, cleaned, compared, or prepared for Shopify import workflows.

## Features

* Exports product data from a single Shopify collection/category URL
* Supports multiple collection URLs from a `.txt` file
* Combines products from multiple selected collections into one CSV
* Uses Shopify’s public `products.json` endpoint when available
* Exports each product variant as a separate CSV row
* Includes product title, URL, description, price, compare-at price, variant title, options, SKU, image URL, availability, source collection, and scrape timestamp
* Supports an optional `--limit` argument
* Handles unavailable JSON endpoints without crashing
* Saves structured CSV output
* Works as a simple command-line tool

## Why This Project

Many Shopify product export tools export the entire store. In real workflows, the user often needs only selected categories or collections, such as:

* Sale items
* Clearance products
* Men’s clothing
* Women’s shoes
* Specific product categories
* Selected collections from multiple stores

This tool is designed as a lightweight first version for exporting products from selected Shopify collections into CSV.

It is especially useful for clothing and footwear stores because product variants such as size, SKU, price, and availability are exported as separate rows.

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
    collections.txt

  README.md
  requirements.txt
  .gitignore
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Single Collection

Export products from one selected Shopify collection:

```bash
python src/main.py data/products.csv --collection-url https://www.allbirds.com/collections/mens --limit 2
```

The `--limit` argument is optional.

Example without limit:

```bash
python src/main.py data/products.csv --collection-url https://www.allbirds.com/collections/mens
```

### Multiple Collections

Create a `.txt` file with one Shopify collection URL per line.

Example `data/collections.txt`:

```text
https://www.allbirds.com/collections/mens
https://www.allbirds.com/collections/womens
```

Run the exporter:

```bash
python src/main.py data/products.csv --collections-file data/collections.txt --limit 2
```

This will export products from all listed collections into one combined CSV file.

## CLI Arguments

```text
output_file
```

Path to the CSV file where results will be saved.

```text
--collection-url
```

A single Shopify collection/category URL.

```text
--collections-file
```

Path to a `.txt` file containing multiple Shopify collection URLs.

```text
--limit
```

Optional product limit per collection. The limit applies to products, not variants.

For example, if `--limit 2` is used and each product has multiple variants, the final CSV may contain more than 2 rows because each variant is exported as a separate row.

## Output Fields

The CSV includes the following columns:

```text
product_title
product_url
description
price
compare_at_price
variant_title
option1
option2
option3
sku
image_url
availability
source_collection
scraped_at
```

## Example Output

```csv
product_title,product_url,description,price,compare_at_price,variant_title,option1,option2,option3,sku,image_url,availability,source_collection,scraped_at
Men's Tree Runner NZ - Natural White,https://www.allbirds.com/products/mens-tree-runner-nz-natural-white,,100.00,,8,8,,,A11914M8,https://cdn.shopify.com/...,True,https://www.allbirds.com/collections/mens,2026-06-25T10:23:06
Men's Tree Runner NZ - Natural White,https://www.allbirds.com/products/mens-tree-runner-nz-natural-white,,100.00,,8.5,8.5,,,A11914M85,https://cdn.shopify.com/...,True,https://www.allbirds.com/collections/mens,2026-06-25T10:23:06
```

## Variant Export

Each product variant is exported as a separate CSV row.

For example, if one product has sizes 8, 8.5, 9, and 9.5, the CSV will contain one row for each size. This makes the output more useful for clothing and footwear stores where size, SKU, price, and availability can differ by variant.

The following fields are variant-specific when available:

```text
price
compare_at_price
variant_title
option1
option2
option3
sku
availability
```

The following fields are shared across variants from the same product:

```text
product_title
product_url
description
image_url
source_collection
scraped_at
```

## Multiple Collections Workflow

The tool supports exporting multiple selected Shopify collections into one CSV.

Example use case:

```text
Store A:
- Sale collection
- Clearance collection

Store B:
- Men's jackets collection
- Women's shoes collection
```

Instead of exporting an entire store, the user can provide only the selected collection URLs in `data/collections.txt`.

The exporter will process each collection URL and combine all product variant rows into a single CSV.

## Notes

Some fields may be empty depending on what the Shopify store exposes through its public product data.

For example:

* `description` may be empty if the store does not expose `body_html`
* `sku` may be empty if product variants do not include SKU values
* `compare_at_price` may be empty if the item is not discounted
* `option2` and `option3` may be empty if the product only has one option, such as size
* `availability` depends on the data exposed by the store

## Current Limitations

This is a lightweight MVP version.

It currently:

* Uses the public Shopify JSON endpoint
* Exports all product variants as separate rows
* Uses the first product image as the main image URL
* Does not yet format output directly into Shopify’s official import CSV template
* Does not include advanced inventory monitoring
* Does not compare inventory between multiple exports
* Does not bypass anti-bot systems, captchas, private APIs, or login-protected stores

## Possible Improvements

Future versions could include:

* Shopify import-ready CSV formatting
* Inventory comparison between multiple exports
* Product handle-based change tracking
* Support for multiple stores with store labels
* HTML fallback if `products.json` is unavailable
* Exporting multiple images per product
* Cleaner formatting for HTML descriptions
* Separate inventory history reports
* Deduplication across overlapping collections

## What I Practiced

* Building a Shopify-specific data extraction workflow
* Working with public Shopify JSON endpoints
* Parsing nested product, image, and variant data
* Exporting all variants as separate rows
* Building product URLs from Shopify handles
* Reading multiple collection URLs from a `.txt` file
* Combining results from multiple selected collections
* Exporting structured CSV files
* Adding optional CLI arguments with `argparse`
* Handling missing fields safely
* Structuring a Python project into clean modules

## Compliance Note

This tool is intended for extracting publicly available product data from accessible Shopify collection pages.

It does not bypass logins, captchas, private APIs, or restricted access systems. Use it only on websites where automated access is allowed and always respect each website’s terms of service and robots.txt.
