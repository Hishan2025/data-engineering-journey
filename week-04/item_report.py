import sales_tools
def parse_record(raw):
    parts = raw.split(";")

    return {
        "order_id":      sales_tools.clean_id(parts[0]),
        "order_date":    parts[1].strip(),
        "customer_name": sales_tools.clean_name(parts[2]),
        "item_name":     parts[3].strip(),
        "quantity":      int(parts[4].strip()),
        "amount":        sales_tools.clean_amount(parts[5]),
        "payment":       parts[6].strip().lower(),
        "status":        parts[7].strip().lower(),
    }


line = "  ord100045 ; 2026-10-07 ;  RAHIM  uddin ; Miniket Chal 5kg ; 2 ; ৳ 1,240.50 ; BKASH ; delivered"

rec = parse_record(line)


with open("raw_sales_week2.txt", encoding="utf-8") as fh:
    lines = fh.read().strip().split("\n")

records = []
cancelled = 0

for raw in lines:
    r = parse_record(raw)
    if r["status"] == "cancelled":
        cancelled = cancelled + 1
        continue
    records.append(r)

print(f"মোট লাইন: {len(lines)}  ·  বাতিল: {cancelled}  ·  হিসাবে: {len(records)}")
print()

def totals_by(records, key):
    totals = {}
    counts = {}

    for rec in records:
        name = rec[key]
        totals[name] = totals.get(name, 0.0) + rec["amount"]
        counts[name] = counts.get(name, 0) + 1
    return totals, counts


totals, counts = totals_by(records, "item_name")
print("পণ্য ধরে হিসাব")
for name in sorted(totals):
    print(f"   {name:<18} {counts[name]}টা   {sales_tools.taka(totals[name])}")
print(f"   {'সব মিলিয়ে':<18} {len(records)}টা   {sales_tools.taka(sum(totals.values()))}")

print()
best = max(totals, key=totals.get)

print(f"সবচেয়ে বেশি বিক্রি: {best} — {sales_tools.taka(totals[best])} ({counts[best]}টা অর্ডার)")