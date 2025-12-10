#!/usr/bin/env python3
import os
import json
import requests
from pathlib import Path

API_KEY = "02LBgUUfWwFri0Cj-oOZu1gVq4aIaEfSTbP7KbP9kyRNCEk9TZqnyX8p9OXvsF49"
SITE_ID = "yuchenguommm.github.io"
PERIOD = "30d"

url = "https://plausible.io/api/v1/stats/breakdown"
params = {
    "site_id": SITE_ID,
    "period": PERIOD,
    # 关键修正：必须是 visit:country，而不是 country
    "property": "visit:country",
    # metrics 可写可不写，不写就默认 visitors
    "metrics": "visitors",
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json",
}


resp = requests.get(url, params=params, headers=headers, timeout=30)
resp.raise_for_status()

data = resp.json()

results = data.get("results", [])
results = sorted(results, key=lambda x: x.get("visitors", 0), reverse=True)

lines = ["countries:"]
for item in results:
    country = item.get("country", "Unknown")
    visitors = item.get("visitors", 0)
    lines.append(f"  - code: {country}")
    lines.append(f"    visitors: {visitors}")

out_path = Path("_data/plausible_stats.yml")
out_path.parent.mkdir(exist_ok=True)

text = "\n".join(lines) + "\n"

old = ""
if out_path.exists():
    old = out_path.read_text(encoding="utf-8")

if text != old:
    out_path.write_text(text, encoding="utf-8")
    print("plausible_stats.yml updated.")
else:
    print("No changes.")
