from urllib.parse import urlparse
from datetime import datetime

def parse_products_from_json(json_data, collection_url, limit=None):
    rows = []
    products = json_data.get("products", [])
    if limit != None:
        products = products[:limit]
        parsed_url = urlparse(collection_url)
        store_base = f"{parsed_url.scheme}://{parsed_url.netloc}"
    for product in products:
        title = product.get("title", "")
        handle = product.get("handle", "")

        if handle:
            product_url = f"{store_base}/products/{handle}"
        else:
            product = ""
        description = product.get("description", "")
        images = product.get("images", [])

        if images:
            first_image = images[0]
            image_url = first_image.get("src", "")
        else:
            image_url = ""

        variants = product.get("variants", [])

        if variants:
            first_variant = variants[0]
            price = first_variant.get("price", "")
            availability = first_variant.get("available", "")
            variant_title = first_variant.get("title", "")
            sku = first_variant.get("sku", "")
            compare_at_price = first_variant.get("compare_at_price")
        else:
            price = ""
            availability = ""

        scraped_at = datetime.now().isoformat(timespec="seconds")

        row = {
        "product_title": title,
        "product_url": product_url,
        "description": description,
        "price": price,
        "compare_at_price": compare_at_price,
        "variant_title": variant_title,
        "sku": sku,      
        "image_url": image_url,
        "availability": availability,
        "source_collection": collection_url,
        "scraped_at": scraped_at
        }
        rows.append(row)

    return rows