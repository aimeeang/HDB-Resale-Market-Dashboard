import pandas as pd
import requests

# Load CSV file
df = pd.read_csv(r'C:\Users\angme\OneDrive\Desktop\Data Analytics\HDBResale_Dataset.csv')  # Update with your file path

# Define the OneMap API endpoint and access token
onemap_url = "https://www.onemap.gov.sg/api/common/elastic/search"
access_token = "UPDATE ACCESS TOKEN HERE"  # Replace with your actual access token

# Function to get coordinates from OneMap API for a given address
def get_address_coordinates(block, street_name):
    address = f"{block} {street_name}"
    params = {
        'searchVal': address,
        'returnGeom': 'Y',
        'getAddrDetails': 'Y',
        'pageNum': 1
    }
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    try:
        response = requests.get(onemap_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        results = response.json()
        if results['found'] > 0:
            best_result = results['results'][0]
            lat = best_result['LATITUDE']
            lon = best_result['LONGITUDE']
            return lat, lon
        else:
            print(f"No results found for address: {address}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None, None
    except KeyError:
        print(f"Unexpected response format for address: {address}")
        return None, None

# Initialize new columns for address coordinates
df['street_latitude'] = None
df['street_longitude'] = None

# Iterate over each row in the dataframe
for idx, row in df.iterrows():
    # Get address coordinates
    address_lat, address_lon = get_address_coordinates(row['block'], row['street_name'])
    # Update address coordinates
    df.at[idx, 'street_latitude'] = address_lat
    df.at[idx, 'street_longitude'] = address_lon

# Save the updated dataframe to a new CSV
df.to_csv(r'C:\Users\angme\OneDrive\Desktop\Data Analytics\HDBResale_Dataset_With_LatLon.csv', index=False)  # Update with your desired file path
