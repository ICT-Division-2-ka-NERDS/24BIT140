for hour in range(24):
    if hour == 0:
        print("12:00 Midnight")
    elif hour == 12:
        print(str(hour)+":00 Noon")
    elif hour < 12:
        print(str(hour)+":00 AM")
    else:
        print(str(hour-12)+":00 PM")
