import requests
import pandas as pd
from io import StringIO
from pathlib import Path

# Toronto Open Data API base URL
base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

# Define the path for saving the data
data_directory = Path("/Users/alexanderguarasci/Documents/GitHub/paper_one/inputs/data")
data_directory.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist

# Retrieve the metadata for the major crime indicators package
url = base_url + "/api/3/action/package_show"
params = {"id": "major-crime-indicators"}

try:
    package = requests.get(url, params=params).json()
    if not package.get("success", False):
        print("Failed to retrieve package data.")
        exit(1)
except requests.exceptions.RequestException as e:
    print(f"Error fetching package data: {e}")
    exit(1)

# Loop through the resources and check which are active
active_resources = []
for resource in package["result"]["resources"]:
    if resource.get("datastore_active", False):
        active_resources.append(resource)

if not active_resources:
    print("No active resources found.")
else:
    print(f"Found {len(active_resources)} active resources.")

# Process each active resource
for idx, resource in enumerate(active_resources):
    # Get all records in CSV format
    csv_url = base_url + "/datastore/dump/" + resource["id"]
    
    try:
        resource_dump_data = requests.get(csv_url).text
        
        # Convert the CSV string to a Pandas DataFrame
        df = pd.read_csv(StringIO(resource_dump_data))
        
        # Save the full DataFrame to CSV in the specified directory
        full_data_file_path = data_directory / f"full_data_{idx}.csv"
        df.to_csv(full_data_file_path, index=False)
        print(f"Full data saved to: {full_data_file_path}")
    except Exception as e:
        print(f"Error processing resource {resource['id']}: {e}")
