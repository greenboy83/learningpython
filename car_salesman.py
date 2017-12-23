amount = float(input("Enter your car's price: "))

tax = amount * 0.1
register_fee = 230
manual_fee = amount * 0.05
shipment_fee = amount * 0.01
total = tax + register_fee + manual_fee + shipment_fee

print("Tax fee is ", tax)
print("Register fee is ", register_fee)
print("Manual fee is ", manual_fee)
print("Shipment fee is ", shipment_fee)
print("Total fee is ", (tax + register_fee + manual_fee + shipment_fee))
