import pandas as pd
import random

random.seed(8)

# Define the number of records to simulate
num_records = 1000

# Define possible offences and location types
offences = [
    "Assault", "B&E", "Robbery With Weapon", "B&E W'Intent", 
    "Unlawfully In Dwelling-House", "Assault Peace Officer", 
    "Theft Over", "Robbery - Purse Snatch", "Robbery - Business", 
    "Assault With Weapon"
]

location_types = [
    "Apartment (Rooming House, Condo)", 
    "Other Commercial / Corporate Places (For Profit, Warehouse, Corp. Bldg)", 
    "Streets, Roads, Highways (Bicycle Path, Private Road)", 
    "Single Home, House (Attach Garage, Cottage, Mobile)", 
    "Bar / Restaurant", 
    "Commercial Dwelling Unit (Hotel, Motel, B & B, Short Term Rental)", 
    "Ttc Subway Station", 
    "Ttc Subway Train"
]

# Define date range (from 2013-12-31 to 2024-06-29)
start_date = pd.to_datetime('2013-12-31')
end_date = pd.to_datetime('2024-06-29')

# Generate random dates
date_range = pd.date_range(start=start_date, end=end_date).to_list()
dates = [random.choice(date_range) for _ in range(num_records)]

# Simulate the data
data = {
    "date": dates,
    "offence": [random.choice(offences) for _ in range(num_records)],
    "location_type": [random.choice(location_types) for _ in range(num_records)],
    "neighbourhood": [random.randint(1, 158) for _ in range(num_records)]  # Neighbourhoods are represented by numbers between 1 and 158
}

# Create a DataFrame with the simulated data
simulated_df = pd.DataFrame(data)

# Save the simulated data to a CSV file
simulated_df.to_csv("outputs/simulated_cleaned_data.csv", index=False)
print("Simulated data saved to simulated_cleaned_data.csv")

# Print the first few rows of the simulated data
print(simulated_df.head())