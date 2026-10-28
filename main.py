import json
import csv
from pathlib import Path


def load_csv():
    file_path = Path(__file__).parent / "data" / "device_telemetry.csv"

    try:
        with file_path.open(mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            return rows

    except FileNotFoundError:
        print(f"Error: CSV file not found at {file_path}")
        return []


def group_by_device(rows):
    devices = {}

    for row in rows:
        device_id = row["device_id"]

        if device_id not in devices:
            devices[device_id] = []

        devices[device_id].append(row)

    return devices

def calculate_statistics(devices):
    summaries = []

    for device_id, records in devices.items():
        temperatures = []
        error_count = 0

        for row in records:
            if row["status"].strip().upper() == "ERROR":
                error_count += 1
                            
            try:
                temperature = float(row["temperature"])
            except (ValueError, TypeError):
                continue

            temperatures.append(temperature)

            

        if not temperatures:
            print(f"Warning: No valid temperatures for {device_id}")
            continue

        total_records = len(records)
        average_temperature = sum(temperatures) / len(temperatures)

        summary = {
            "device_id": device_id,
            "total_records": total_records,
            "average_temperature": round(average_temperature, 2),
            "error_count": error_count
        }

        summaries.append(summary)

    return summaries





if __name__ == "__main__":
    rows = load_csv()
    devices = group_by_device(rows)
    summaries = calculate_statistics(devices)

    filtered_summaries = []

    for summary in summaries:
        if summary["average_temperature"] <= 80.0:
            filtered_summaries.append(summary)

    # Export filtered summaries to JSON
    output_path = Path(__file__).parent / "output" / "device_summary.json"

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(filtered_summaries, file, indent=4)

    print(f"JSON report saved to: {output_path}")

    # Print summaries
    
print("\nDevice Summary")
print("-" * 55)
print(f"{'Device ID':<15}{'Records':<12}{'Avg Temp':<15}{'Errors':<10}")
print("-" * 55)

for summary in filtered_summaries:
    print(
        f"{summary['device_id']:<15}"
        f"{summary['total_records']:<12}"
        f"{summary['average_temperature']:<15.2f}"
        f"{summary['error_count']:<10}"
    )

print("-" * 55)




