# AI Prompt Log

## 1. Initial Prompt

Help me create a Python script using Matplotlib that reads device summaries from a JSON file and generates a bar chart showing average temperature by device. Explain the code step by step.

## 2. Bug or Formatting Issue

**Issue:** Device labels on the horizontal axis may overlap or become difficult to read when device IDs are long or when the dataset contains many devices.

**Fix:** Added `plt.xticks(rotation=45)` to rotate the horizontal-axis labels and improve readability.

## 3. Follow-up Prompt

How can I improve the readability of the device labels on my Matplotlib bar chart when the labels are long or overlap? Explain the change and show where to place the code.