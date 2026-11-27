import csv
import os

from item_report import parse_record

os.makedirs("output", exist_ok=True)

records = []

COLUMNS = [
    "order_id",
    "order_date",
    "customer_name",
    "item_name",
    "quantity",
    "amount",
    "payment",
    "status"
]

with open("raw_sales_week2.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        rec = parse_record(line)
        if rec["status"] == "cancelled":
            continue
        records.append(rec)

with open("output/sales_week2_clean.csv", "w",
          encoding="utf-8", newline="") as fh:

    writer = csv.DictWriter(fh, fieldnames=COLUMNS)
    writer.writeheader()

    for rec in records:
        writer.writerow(rec)

print("লেখা হলো — output/sales_week2_clean.csv")
print()
print(open("output/sales_week2_clean.csv", encoding="utf-8").read())
print()
print(f"লেখা হলোঃ week-04/output/sales_week2_clean.csv   ({len(records)}টা সারি + হেডার)")


totals = {}

for rec in records:
    item = rec["item_name"]
    if item not in totals:        
        totals[item] = {"orders": 0, "total_amount": 0.0}
    totals[item]["orders"] += 1
    totals[item]["total_amount"] += rec["amount"]

SUMMARY_COLUMNS = ["item_name", "orders", "total_amount"]

with open("output/item_summary.csv", "w", encoding="utf-8", newline="") as fh:
    writer = csv.DictWriter(fh, fieldnames=SUMMARY_COLUMNS)
    writer.writeheader()

    for item in sorted(totals):
        writer.writerow ({
            "item_name": item,
            "orders": totals[item]["orders"],
            "total_amount": round(totals[item]["total_amount"], 2),
        })

print(f"লেখা হলো: week-04/output/item_summary.csv       ({len(totals)}টা সারি + হেডার)")
print()
grand_total = sum(rec["amount"] for rec in records)
print(f"CSV থেকে ফেরত পড়লাম: {len(records)}টা record")
print(f"সব মিলিয়ে: ৳{grand_total:.2f}")