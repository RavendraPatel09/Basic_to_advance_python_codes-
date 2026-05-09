def check_fever(temp_celsius):
    if temp_celsius >= 39.5:
        return "High Fever - Seek Medical Attention"
    elif temp_celsius >= 37.5:
        return "Mild Fever - Rest and Hydrate"
    else:
        return "Normal Temperature"

print(check_fever(38.2))