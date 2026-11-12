raw_a = "  ord100047 ;2026-10-08;  Tanvir Hossain  ; Dim 12pc ;3; ৳ 441.75 ; Cash on Delivery ;DELIVERED"
raw_b = "ORD100048 ; 2026-10-08 ; SUMAIYA  KHAN ; Ilish 1kg ;1;৳ 1,520.00; bkash ; cancelled"
raw_c = "ord100049;2026-10-09; rakib  mia ;Broiler Murgi 1kg; 4 ;৳ 812.00;Card;delivered"

parts = raw_b.split(";")
order_id = parts[0]
order_date = parts[1]
customer_name = parts[2]
item_name = parts[3]
quantity_text = parts[4]
amount_text = parts[5]
payment = parts[6]
status = parts[7]
customer_name = customer_name.replace("  ", " ").strip().title()
quantity = int(quantity_text)
print("সতর্কতা: এই অর্ডারটা বাতিল হয়েছে, হিসাবে ধরবেন না।")



