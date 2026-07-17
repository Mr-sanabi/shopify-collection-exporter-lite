from urllib.parse import urlparse
from datetime import datetime

def parse_products_from_json(json_data, collection_url, limit=None):
    rows = []
    products = json_data.get("products", [])
    parsed_url = urlparse(collection_url)
    store_base = f"{parsed_url.scheme}://{parsed_url.netloc}"
    if limit is not None:
        products = products[:limit] 
    for product in products:
        title = product.get("title", "")
        handle = product.get("handle", "")

        if handle:
            product_url = f"{store_base}/products/{handle}"
        else:
            product_url = ""
        images = product.get("images", [])
        description = product.get("body_html", "")
        if not description:
            description = product.get("description", "")

        if not description:
            description = ""
       

        if images:
            first_image = images[0]
            image_url = first_image.get("src", "")
        else:
            image_url = ""

        variants = product.get("variants", [])
        scraped_at = datetime.now().isoformat(timespec="seconds")

        if variants:
            for variant in variants:
                price = variant.get("price", "")
                availability = variant.get("available", "")
                variant_title = variant.get("title", "")
                sku = variant.get("sku", "")
                compare_at_price = variant.get("compare_at_price", "")
                option1 = variant.get("option1", "")
                option2 = variant.get("option2", "")
                option3 = variant.get("option3", "")

                row = {
                    "product_title": title,
                    "product_url": product_url,
                    "description": description,
                    "price": price,
                    "compare_at_price": compare_at_price,
                    "variant_title": variant_title,
                    "option1": option1,
                    "option2": option2,
                    "option3": option3,
                    "sku": sku,
                    "image_url": image_url,
                    "availability": availability,
                    "source_collection": collection_url,
                    "scraped_at": scraped_at
                }

                rows.append(row)

        else:
            row = {
                "product_title": title,
                "product_url": product_url,
                "description": description,
                "price": "",
                "compare_at_price": "",
                "variant_title": "",
                "option1": "",
                "option2": "",
                "option3": "",
                "sku": "",
                "image_url": image_url,
                "availability": "",
                "source_collection": collection_url,
                "scraped_at": scraped_at
            }

            rows.append(row)
    return rows