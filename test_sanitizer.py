
from sanitizer import clean_sensor_readings

# Test 1: Mixed valid and invalid readings
readings = [25, "45.5", None, -10, "invalid", 600, 100]
result = clean_sensor_readings(readings)
print("Test 1:", result)

# Test 2: Empty list
readings = []
result = clean_sensor_readings(readings)
print("Test 2:", result)

# Test 3: All invalid readings
readings = [None, -5, "hello"]
result = clean_sensor_readings(readings)
print("Test 3:", result)
