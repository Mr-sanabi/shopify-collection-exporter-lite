from src.parser import parse_products_from_json

def test_parse_without_limit():
    collection_url = "https://store.example/collections/running-shoes"

    json_data = {
        "products": [
            {
                "id": 101,
                "title": "Trail Runner",
                "handle": "trail-runner",
                "vendor": "Example Sports",
                "product_type": "Shoes",
                "body_html": "<p>Running shoes for trails.</p>",
                "images": [
                    {
                        "src": "https://cdn.example/trail-runner.jpg"
                    }
                ],
                "variants": [
                    {
                        "id": 1001,
                        "title": "Default Title",
                        "sku": "TRAIL-001",
                        "price": "79.99",
                        "available": True,
                    }
                ],
            }
        ]
    }
    result = parse_products_from_json(json_data, collection_url)
    assert len(result) == 1

def test_missing_handle_has_empty_url():
    collection_url = "https://store.example/collections/accessories"

    json_data = {
        "products": [
            {
                "id": 202,
                "title": "Travel Bottle",
                "body_html": "<p>Reusable travel bottle.</p>",
                "images": [],
                "variants": [
                    {
                        "id": 2001,
                        "title": "Default Title",
                        "sku": "BOTTLE-001",
                        "price": "15.00",
                        "available": True,
                    }
                ],
            }
        ]
    }

    result = parse_products_from_json(json_data, collection_url)
    assert result[0]["product_url"] == ""

def test_body_html_used_as_description():
    collection_url = "https://store.example/collections/jackets"

    json_data = {
        "products": [
            {
                "id": 303,
                "title": "Rain Jacket",
                "handle": "rain-jacket",
                "body_html": "<p>Primary Shopify description.</p>",
                "description": "Old fallback description",
                "images": [],
                "variants": [
                    {
                        "id": 3001,
                        "title": "Default Title",
                        "sku": "JACKET-001",
                        "price": "120.00",
                        "available": True,
                    }
                ],
            }
        ]
    }

    result = parse_products_from_json(json_data, collection_url)
    assert result[0]["description"] == (
        "<p>Primary Shopify description.</p>"
    )
    