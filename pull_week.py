import os
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

# URL of the XML
url = "https://nfs.faireconomy.media/ff_calendar_thisweek.xml"

# List of keywords to search for in the title
keywords = [
    "CPI ",
    "Core Retail",
    "Fed Chair",
    "Prelim UoM Consumer Sentiment",
    "ISM Services PMI",
    "Unemployment Claims"
]


def get_current_monday():
    today = datetime.now()
    # Calculate the date of the current Monday
    monday = today - timedelta(days=today.weekday())
    return monday


def fetch_and_parse_xml(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
        return ET.fromstring(response.content)
    else:
        print(f"Failed to fetch XML. Status code: {response.status_code}")
        return None


def save_matching_dates(root, output_file="matching_dates.txt"):
    matching_dates = []

    for event in root.findall(".//event"):
        country = event.find("country").text
        impact = event.find("impact").text.strip()
        title = event.find("title").text
        date_str = event.find("date").text.strip()

        # Check the conditions
        if country == "USD" and impact == "High" and any(keyword in title for keyword in keywords):
            # Parse the date and add one day
            date_obj = datetime.strptime(date_str, "%m-%d-%Y")
            new_date_obj = date_obj + timedelta(days=1)
            new_date_str = new_date_obj.strftime("%Y-%m-%d")

            # Append the new date string to the matching dates list
            matching_dates.append(new_date_str)

    # Append the dates to the existing file
    if matching_dates:
        with open(output_file, "a") as f:  # Open the file in append mode
            for date in matching_dates:
                f.write(date + "\n")
        print(f"Matching dates appended to {output_file}")
    else:
        print("No matching events found.")


def main():
    # Calculate the current Monday's date
    current_monday = get_current_monday()
    formatted_monday = current_monday.strftime("%m-%d-%Y")
    filename = f"this_week_{formatted_monday}.xml"

    # Check if the file already exists
    if not os.path.exists(filename):
        print(f"{filename} not found. Downloading XML...")
        root = fetch_and_parse_xml(url, filename)
    else:
        print(f"{filename} found. Parsing existing XML file.")
        tree = ET.parse(filename)
        root = tree.getroot()

    if root:
        save_matching_dates(root)


if __name__ == "__main__":
    main()