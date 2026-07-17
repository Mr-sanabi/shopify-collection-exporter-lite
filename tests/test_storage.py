from src.storage import save_csv
import csv

def test_save_csv_creates_parent_directory(tmp_path):
    records = [
        {
            "title": "Trail Runner",
            "price": "79.99",
        },
        {
            "title": "Rain Jacket",
            "price": "120.00",
        },
    ]
    file_path = tmp_path / "nested" / "processed" / "products.csv"
    save_csv(file_path, records)
    assert file_path.exists()
    assert not file_path == "product.csv.tmp"
    with open (file_path, "r",encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    assert rows == records
