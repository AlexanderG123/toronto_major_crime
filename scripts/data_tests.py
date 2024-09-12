import pandas as pd
import pytest

# Define the file path for the simulated data
file_path = "outputs/simulated_cleaned_data.csv"

# Load the data
data = pd.read_csv(file_path)

def test_date_range():
    """Test that all dates are within the specified range"""
    start_date = pd.to_datetime('2013-12-31')
    end_date = pd.to_datetime('2024-06-29')
    dates = pd.to_datetime(data["date"])
    assert dates.min() >= start_date, "Dates contain values before the start date."
    assert dates.max() <= end_date, "Dates contain values after the end date."

def test_neighbourhood_range():
    """Test that all neighbourhood values are between 1 and 158"""
    neighbourhoods = data["neighbourhood"]
    assert neighbourhoods.min() >= 1, "Neighbourhood values contain numbers less than 1."
    assert neighbourhoods.max() <= 158, "Neighbourhood values contain numbers greater than 158."

def test_column_non_null():
    """Test that there are no null values in critical columns"""
    assert data["date"].notnull().all(), "Date column contains null values."
    assert data["offence"].notnull().all(), "Offence column contains null values."
    assert data["location_type"].notnull().all(), "Location type column contains null values."
    assert data["neighbourhood"].notnull().all(), "Neighbourhood column contains null values."

def test_unique_records():
    """Test that the dataset does not contain duplicate rows"""
    assert data.duplicated().sum() == 0, "Dataset contains duplicate rows."

# To run the tests, use pytest in your command line
if __name__ == "__main__":
    pytest.main()