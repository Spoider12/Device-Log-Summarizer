
def clean_sensor_readings(readings):
    cleaned_readings = []

    for value in readings:
        try:
            number = float(value)
        except (ValueError, TypeError):
            continue

        if number < 0:
            continue

        if number > 500.0:
            number = 500.0

        cleaned_readings.append(number)

    return cleaned_readings
