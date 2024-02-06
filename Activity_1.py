sale_price = float(input("Enter sale price: "))

tax_rate = float(input("Enter tax rate: "))

sales_tax = sale_price * tax_rate / 100

final_price = sale_price + sales_tax

print("Sale Price", sale_price, "Tax rate", tax_rate, "Sales tax", sales_tax, "Final price", final_price)