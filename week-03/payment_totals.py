import os

PATH = os.path.join("module-02", "data", "raw_sales.txt")

with open(PATH, encoding="utf-8") as fh:
    lines = fh.read().strip().split("\n")


# ============================================================
#  লেভেল ১ — শুধু bkash
#  লক্ষ্য:  bkash  3টা  ৳2484.00
# ============================================================

bkash_total = 0.0
bkash_count = 0

for raw in lines:
    parts   = raw.split(";")
    amount  = float(parts[5].strip().replace("৳", "").replace(",", ""))
    payment = parts[6].strip().lower()
    status  = parts[7].strip().lower() 

     
    if status == "cancelled":
        continue
        

     
    if payment == "bkash":
        bkash_total = bkash_total + amount
        bkash_count = bkash_count + 1

    



print("লেভেল ১")
print(f"bkash  {bkash_count}টা  ৳{bkash_total:.2f}")
print()
