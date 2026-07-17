import csv
from pathlib import Path

def save_csv(output_file, rows):
    if not rows:
        print("No products found. CSV was not created.")
        return
    
    path = Path(output_file)
    path.parent.mkdir(parents=True, exist_ok=True)

    
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    fields = rows[0].keys()

    with open(temporary_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    temporary_path.replace(path)