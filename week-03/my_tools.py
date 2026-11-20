def clean_amount(text):
    text = text.replace("৳", "").replace(",", "").strip()
    return float(text)

def taka(amount):
    return f"৳{amount:.2f}"


if __name__ == "__main__":
    print(clean_amount("৳ 1,240.50"))
    print(taka(1240.5))
