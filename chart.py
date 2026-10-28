
import json
from pathlib import Path
import matplotlib.pyplot as plt


# Locate the JSON file
file_path = Path(__file__).parent / "output" / "device_summary.json"

# Read the JSON data
with file_path.open("r", encoding="utf-8") as file:
    data = json.load(file)

print(data)


# Extract device IDs and average temperatures
device_ids = []
average_temperatures = []

for item in data:
    device_ids.append(item["device_id"])
    average_temperatures.append(item["average_temperature"])

print("Device IDs:", device_ids)
print("Average temperatures:", average_temperatures)


# Create the bar chart
plt.figure(figsize=(8, 5))

plt.bar(device_ids, average_temperatures)

plt.title("Average Temperature by Device")
plt.xlabel("Device ID")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
