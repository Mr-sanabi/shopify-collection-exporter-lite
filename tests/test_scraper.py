import sys

sys.path.insert(0, "src")

import scraper

def test_fetch_failure_returns_empty_list(monkeypatch):
    monkeypatch.setattr(
        scraper,
        "fetch_json",
        lambda url: None
    )

    result = scraper.scrape_collection(
        "https://store.example/collections/shoes"
    )
    assert result == []