from decimal import Decimal

order_total = Decimal("100.05")
discount_percent = Decimal(".1")
discount = order_total * discount_percent

subtotal = order_total - discount
tax_percent = Decimal(".08")
sales_tax = subtotal * tax_percent
invoice_total = subtotal + sales_tax

print("{:15} {:>10.6}".format("Order Total: ", str(order_total)))
print("{:15} {:>10.5}".format("Discount:", str(discount)))
print("{:15} {:>10.5}".format("Subtotal:", str(subtotal)))
print("{:15} {:>10.4}".format("Sales Tax:", str(sales_tax)))
print("{:15} {:>10.5}".format("Invoice Total:", str(invoice_total)))