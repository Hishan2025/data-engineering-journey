
import os
import my_tools



def clean_amount(text):
    text = text.replace("৳", "").replace(",", "").strip()
    return float(text)


def taka(amount):
    return f"৳{amount:.2f}"


def read_lines(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read().strip().splitlines()
        


def main():

    PATH = os.path.join("module-02", "data", "raw_sales.txt")

    lines = read_lines(PATH)

    bkash_total = nagad_total = card_total = rocket_total = cash_total = 0.0
    bkash_count = nagad_count = card_count = rocket_count = cash_count = 0

    for raw in lines:

        parts = raw.split(";")

        amount = my_tools.clean_amount(parts[5])        
        payment = parts[6].strip().lower()
        status = parts[7].strip().lower()

        if status == "cancelled":
            continue

        if payment == "bkash":
            bkash_total += amount
            bkash_count += 1

        elif payment == "nagad":
            nagad_total += amount
            nagad_count += 1

        elif payment == "card":
            card_total += amount
            card_count += 1

        elif payment == "rocket":
            rocket_total += amount
            rocket_count += 1

        else:
            cash_total += amount
            cash_count += 1

    grand_total = bkash_total + nagad_total + card_total + rocket_total + cash_total

    print(f"bkash  {bkash_count}টা  {taka(bkash_total)}")
    print(f"nagad  {nagad_count}টা  {taka(nagad_total)}")
    print(f"card   {card_count}টা  {taka(card_total)}")
    print(f"rocket {rocket_count}টা  {taka(rocket_total)}")
    print(f"cash on delivery   {cash_count}টা  {taka(cash_total)}")

    print()
    print(f"সব মিলিয়ে: {taka(grand_total)}")


if __name__ == "__main__":
    main()

