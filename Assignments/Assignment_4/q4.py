Item= "Art Supplies"
Unit_Price= 15.5
Quantity= 100
Tax_rate=5
subtotal= Unit_Price*Quantity
tax_amount=subtotal*0.05
final_total=subtotal+tax_amount
print(f"The Subtotal is:{subtotal:.2f}")
print(f"The Tax amount is:{tax_amount:.2f}")
print(f"The Final Total is:{final_total:.2f}")
