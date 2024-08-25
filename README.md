# Economic Calendar Event Scraper

This Python script downloads and parses an XML file containing economic calendar events for the current week. It identifies and saves the dates of events that match specified criteria, such as high-impact events in the United States with specific keywords in their titles.

## Features

- Downloads the XML file for the current week's economic events.
- Parses the XML to find events that:
  - Occur in the United States (USD).
  - Have a high impact.
  - Contain specific keywords in the title.
- Saves the dates of the matching events to a text file.

## Keywords Searched

The script looks for events with the following keywords in their titles:

- CPI
- Core Retail
- Fed Chair
- Prelim UoM Consumer Sentiment
- ISM Services PMI
- Unemployment Claims

## How It Works

1. **Download XML File**: The script first calculates the current Monday's date and checks if the corresponding XML file for the week is already downloaded. If not, it downloads the XML file from the specified URL.

2. **Parse and Filter Events**: The script then parses the XML file and looks for events that meet the following criteria:
   - The event country is `USD`.
   - The event has a `High` impact.
   - The event title contains any of the specified keywords.

3. **Save Matching Dates**: For each matching event, the script extracts the event date, adds one day, and saves the new date in a text file named `matching_dates.txt`.

## Usage

### Prerequisites

- Python 3.7+
- The `requests` library: Install it using `pip install requests`.

### Running the Script

1. Clone the repository or download the script file.

2. Run the script:
   ```bash
   python script_name.py
