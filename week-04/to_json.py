import json
import os

from item_report import parse_record

os.makedirs("output", exist_ok=True)

records = []
cancelled = 0

with open("raw_sales_week2.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        rec = parse_record(line)

        if rec["status"] == "cancelled":
            cancelled += 1
            continue

        records.append(rec)


item_amount = {}
item_orders = {}
date_amount = {}

for rec in records:
    item = rec["item_name"]
    date = rec["order_date"]

    item_amount[item] = item_amount.get(item, 0.0) + rec["amount"]
    item_orders[item] = item_orders.get(item, 0) + 1
    date_amount[date] = date_amount.get(date, 0.0) + rec["amount"]


top_name = max(item_amount, key=item_amount.get)

report = {
    "company": "ThelaGari",
    "week": "2026-10-12 → 2026-10-18",
    "counted": len(records),
    "cancelled": cancelled,
    "grand_total": round(sum(item_amount.values()), 2),
    "top_item": {
        "item_name": top_name,
        "orders": item_orders[top_name],
        "total_amount": round(item_amount[top_name], 2),
    },
    "by_item": {k: round(item_amount[k], 2) for k in sorted(item_amount)},
    "by_date": {k: round(date_amount[k], 2) for k in sorted(date_amount)},
}

with open("output/report_week2.json", "w", encoding="utf-8") as fh:
    json.dump(report, fh, ensure_ascii=False, indent=2)


with open("output/report_week2.json", "r", encoding="utf-8") as fh:
    report = json.load(fh)


print(type(report["grand_total"]))
print(report["top_item"]["item_name"])
