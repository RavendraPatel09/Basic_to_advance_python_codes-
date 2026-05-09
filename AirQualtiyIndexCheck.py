def aqi_alert(aqi_level):
    if aqi_level > 300:
        return "Hazardous: Stay indoors."
    elif aqi_level > 150:
        return "Unhealthy: Reduce outdoor exertion."
    elif aqi_level > 50:
        return "Moderate: Acceptable air quality."
    else:
        return "Good: Ideal conditions for outdoor activities."

print(aqi_alert(180))