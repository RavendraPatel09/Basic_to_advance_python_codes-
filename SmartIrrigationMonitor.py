import random

def smart_irrigation_controller(moisture_level, rain_probability):
    """
    Decides whether to turn on the water based on environmental data.
    - moisture_level: 0% (bone dry) to 100% (saturated)
    - rain_probability: 0% to 100% chance of rain today
    """
    
    print(f"--- System Status: Moisture {moisture_level}% | Rain Chance {rain_probability}% ---")
    if moisture_level < 30 and rain_probability < 50:
        return "ACTION: Turn Sprinklers ON (Conserving water by checking forecast)."
    
    elif moisture_level < 30 and rain_probability >= 50:
        return "ACTION: Keep Sprinklers OFF (Waiting for free rain water!)"
    
    else:
        return "ACTION: Keep Sprinklers OFF (Soil is already healthy)."
test_days = [
    {"moisture": 20, "rain": 10}, 
    {"moisture": 15, "rain": 85}, 
    {"moisture": 75, "rain": 5}  
]
for day in test_days:
    result = smart_irrigation_controller(day["moisture"], day["rain"])
    print(result + "\n")
    #to run this 