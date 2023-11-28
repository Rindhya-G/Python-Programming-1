fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves = int(input("Enter the number of day-old loaves purchased: "))
price_per_loaf = 185.00
regular_price = fresh_loaves * price_per_loaf
discount = day_old_loaves * price_per_loaf * 0.4
total_price = regular_price + discount
print("regular Price:",regular_price,"rupees")
print("discount:",discount,"rupees")
print("total price:",total_price,"rupees")
