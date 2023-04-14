import pandas as pd
import math

# Function to calculate haversine distance
def haversine_distance(lat1, lon1, lat2, lon2):
    # Convert coordinates from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c  # Earth's radius in km

    return distance

# Function to calculate duration based on distance
def haversine_duration(distance):
    # Assuming an average speed of 20 km/h for buses
    speed = 20
    duration = distance / speed

    return duration

# Create bus stop table
bus_stop_table = pd.DataFrame({'stop_name': ['Gateway of India', 'Churchgate Station', 'Bandra Kurla Complex', 'Juhu Beach', 'Andheri Station', 'Chhatrapati Shivaji Terminal', 'Marine Drive', 'Worli Sea Face', 'Haji Ali Dargah', 'Siddhivinayak Temple', 'Dadar Station', 'Powai Lake'],
                               'latitude': [18.9219, 18.9353, 19.0671, 19.1077, 19.1197, 18.9402, 18.9446, 18.9938, 18.9820, 19.0177, 19.0209, 19.1190],
                               'longitude': [72.8343, 72.8277, 72.8694, 72.8262, 72.8464, 72.8528, 72.8236, 72.7936, 72.8155, 72.8309, 72.8426, 72.9080]})

# Create buses table
buses_table = pd.DataFrame({'Bus Number': ['BUS123', 'BUS456', 'BUS789', 'BUS101', 'BUS234', 'BUS567', 'BUS890', 'BUS111','BUS222', 'BUS333', 'BUS444', 'BUS555'],
                            'Bus Stop': ['Gateway of India', 'Churchgate Station', 'Bandra Kurla Complex', 'Juhu Beach', 'Andheri Station', 'Chhatrapati Shivaji Terminal', 'Marine Drive', 'Worli Sea Face', 'Haji Ali Dargah', 'Siddhivinayak Temple', 'Dadar Station', 'Powai Lake'],
                            'Distance (km)': [5.6, 7.2, 12.3, 9.5, 6.8, 10.1, 8.4, 11.7, 14.2, 7.5, 10.3, 8.9],
                            'Duration (min)': [15, 20, 30, 25, 18, 35, 22, 28, 40, 20, 25, 30]})

# User input for start and end locations
start_location = input("Enter start location: ")
end_location = input("Enter end location: ")
# Get buses around start location
buses_around_start = buses_table[buses_table['Bus Stop'] == start_location]

# Display buses around start location
print(f"Buses around {start_location}:")
print(buses_around_start)

# Get latitude and longitude of start location and end location
start_latitude = bus_stop_table[bus_stop_table['stop_name'] == start_location]['latitude'].iloc[0]
start_longitude = bus_stop_table[bus_stop_table['stop_name'] == start_location]['longitude'].iloc[0]
end_latitude = bus_stop_table[bus_stop_table['stop_name'] == end_location]['latitude'].iloc[0]
end_longitude = bus_stop_table[bus_stop_table['stop_name'] == end_location]['longitude'].iloc[0]


# Calculate distance using Haversine formula (assuming Earth radius as 6371 km)
import math
radius = 6371
delta_latitude = math.radians(end_latitude - start_latitude)
delta_longitude = math.radians(end_longitude - start_longitude)
a = math.sin(delta_latitude/2)**2 + math.cos(math.radians(start_latitude)) * math.cos(math.radians(end_latitude)) * math.sin(delta_longitude/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
distance_km = radius * c

# Display distance between start location and end location
print(f"Distance between {start_location} and {end_location} is {distance_km:.2f} km")

# Calculate fare based on distance
fare = buses_around_start['Fare (INR)'].iloc[0]
fare_incurred = fare * distance_km

# Display fare incurred
print(f"Fare incurred is {fare_incurred:.2f} INR")
