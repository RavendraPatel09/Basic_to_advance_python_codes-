def shipping_cost(weight_kg, distance_km):
    base_fee = 5.00
    weight_fee = weight_kg * 1.50
    distance_fee = distance_km * 0.05
    return base_fee + weight_fee + distance_fee

print(shipping_cost(4.5, 300))
print(shipping_cost(10, 150))
print(shipping_cost(2, 50))
