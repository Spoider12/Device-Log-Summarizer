# Device Log Summarizer CLI

A Python command-line tool that processes device telemetry data from a CSV file, calculates device-level statistics, filters devices based on average temperature, exports summaries to JSON, and generates a temperature chart using Matplotlib.

## Features

- **Sensor Data Cleaning:** Converts valid readings to floats, removes invalid, missing, and negative values, and clips values above 500.0.
- **CSV Processing:** Reads device telemetry records and groups them by device ID.
- **Device Statistics:** Calculates total records, average temperature, and the number of ERROR records for each device.
- **Temperature Filtering:** Excludes devices whose average temperature is greater than 80.0°C.
- **JSON Export:** Saves filtered device summaries to a JSON file.
- **Terminal Summary:** Displays the results in a readable table.
- **Data Visualization:** Generates a bar chart showing average temperature by device.

## Technologies Used

- Python
- CSV and JSON modules
- Matplotlib
- `unittest` for testing the sensor-cleaning function

## Project Structure

```text
device-log-summarizer/
├── data/
│   └── device_telemetry.csv
├── output/
│   └── device_summary.json
├── sanitizer.py
├── test_sanitizer.py
├── main.py
├── chart.py
├── requirements.txt
├── PROMPT_LOG.md
├── README.md
└── .gitignore
```

The `venv/` directory is used for the local Python virtual environment and should not be committed to GitHub.

## Prerequisites

- Python 3.10 or newer
- pip

## Setup and Installation

1. Clone the repository or download the project files.

2. Open a terminal in the project directory.

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment.

   **Windows PowerShell:**

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **Windows Command Prompt:**

   ```cmd
   venv\Scripts\activate.bat
   ```

5. Install the required dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Input Data

Place the telemetry CSV file at:

`data/device_telemetry.csv`

The CSV must contain these columns:

| Column | Description |
|---|---|
| `device_id` | Identifier for the device |
| `status` | Device status, such as ACTIVE, WARNING, or ERROR |
| `temperature` | Temperature reading |

Example:

```csv
device_id,status,temperature
DEV_A,ACTIVE,45
DEV_A,ERROR,55
DEV_A,WARNING,50
DEV_B,ACTIVE,90
DEV_B,ERROR,85
DEV_C,ACTIVE,35
DEV_C,WARNING,40
```

## How to Run

### 1. Run the device log summarizer

```bash
python main.py
```

This reads the CSV file, calculates device statistics, filters devices with average temperatures above 80.0°C, exports the results, and prints a summary table.

### 2. View the JSON report

After running `main.py`, open:

`output/device_summary.json`

The report contains the filtered device summaries.

### 3. Generate the temperature chart

```bash
python chart.py
```

This reads the JSON report and displays a bar chart of average temperature by device.

### 4. Run the tests

```bash
python -m unittest test_sanitizer.py
```

This runs the sensor-cleaning test cases.

## Output

The program generates:

- A terminal summary table
- `output/device_summary.json`
- A Matplotlib bar chart showing average temperature by device

Devices with average temperatures greater than 80.0°C are excluded from the filtered report.

## AI Collaboration

AI assistance was used during development to help explain Python concepts, implement chart generation, review formatting, and troubleshoot errors. The prompts, identified issue, and follow-up interaction are documented in `PROMPT_LOG.md`.

## Notes

- The `output/` directory must exist before running the current JSON export code.
- The input CSV must use the expected column names.
- Invalid temperature readings are skipped when calculating averages.
- Devices without valid temperatures are omitted from the calculated summaries.
