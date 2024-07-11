import pandas as pd
import requests
import math
import time

# Calculate walking and driving times using OneMap API
def get_travel_time(start_lat, start_lon, end_lat, end_lon, route_type, token):
    url = "https://www.onemap.gov.sg/api/public/routingsvc/route"
    
    headers = {
        'Authorization': f'Bearer {token}'
    }

    params = {
        'start': f"{start_lat},{start_lon}",
        'end': f"{end_lat},{end_lon}",
        'routeType': route_type,  # 'walk' for walking, 'drive' for driving
    }

    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                data = response.json()
                if data and 'route_summary' in data:
                    return data['route_summary']['total_time']  # Time in minutes
                else:
                    return None
            else:
                print(f"Error {response.status_code}: {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1}/{max_retries} failed: {e}")
            time.sleep(2)  # Wait for 2 seconds before retrying

    return None

# Load MRT station data
mrt_stations = pd.read_csv(r'C:\Users\angme\OneDrive\Desktop\DatasetNEW\mrt_lrt_data.csv')  # Ensure this file contains columns 'station_name', 'lat', 'lng'

# Load raw data
raw_data = pd.read_csv(r'C:\Users\angme\OneDrive\Desktop\Data Analytics\HDBResale_Dataset_With_LatLon.csv')  

# Calculate travel times
def calculate_travel_times(row, token):
    lat1, lon1 = row['street_latitude'], row['street_longitude']
    nearest_station = mrt_stations[mrt_stations['station_name'] == row['nearest_station']].iloc[0]
    lat2, lon2 = nearest_station['lat'], nearest_station['lng']
    
    walk_time = get_travel_time(lat1, lon1, lat2, lon2, 'walk', token)
    drive_time = get_travel_time(lat1, lon1, lat2, lon2, 'drive', token)
    
    # Calculate distance using Haversine formula
    radius = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    
    return pd.Series({
        'walk_time': walk_time,  # Walking time in minutes
        'drive_time': drive_time,  # Driving time in minutes
        'distance_km': distance  # Distance in kilometers
    })

# Replace with your OneMap API key
api_key = 'ACCESS TOKEN CODE HERE'

# Apply the function to the raw data
raw_data[['walk_time', 'drive_time', 'distance_km']] = raw_data.apply(calculate_travel_times, axis=1, token=api_key)

# Save the results to a new file
raw_data.to_csv(r'C:\Users\angme\OneDrive\Desktop\Data Analytics\HDBResale_Dataset_With_LatLon_Time.csv', index=False)

print("File saved as 'HDBResale_Dataset_With_LatLon_Time.csv'")

