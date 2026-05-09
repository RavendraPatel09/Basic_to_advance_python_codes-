def target_heart_rate(age):
    max_hr = 220 - age
    moderate_zone_low = max_hr * 0.50
    moderate_zone_high = max_hr * 0.70
    return moderate_zone_low, moderate_zone_high

print(target_heart_rate(45))