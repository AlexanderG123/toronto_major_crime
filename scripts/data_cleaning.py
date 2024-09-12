import requests
import pandas as pd
from io import StringIO

# Toronto Open Data API base URL
base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

# Retrieve the metadata for the major crime indicators package
url = base_url + "/api/3/action/package_show"
params = {"id": "major-crime-indicators"}
package = requests.get(url, params=params).json()

# Columns to keep
columns_to_keep = ["OCC_DATE", "OFFENCE", "LOCATION_TYPE", "NEIGHBOURHOOD_158"]

# Loop through the resources
for idx, resource in enumerate(package["result"]["resources"]):

    # Check if the resource is datastore_active
    if resource["datastore_active"]:

        # Get all records in CSV format
        url = base_url + "/datastore/dump/" + resource["id"]
        resource_dump_data = requests.get(url).text
        # Convert the CSV string to a Pandas DataFrame
        df = pd.read_csv(StringIO(resource_dump_data))
        # Clean the data by keeping only the specified columns
        if all(col in df.columns for col in columns_to_keep):
            cleaned_df = df[columns_to_keep]

            # Rename columns for better clarity
            cleaned_df.columns = ["date", "offence", "location_type", "neighbourhood"]

            # Save the cleaned DataFrame to CSV
            cleaned_df.to_csv("outputs/cleaned_data.csv", index=False)
            print("Cleaned data saved to cleaned_data.csv")
        else:
            print("Some required columns are missing in the dataset.")