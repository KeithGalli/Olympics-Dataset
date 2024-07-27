import pandas as pd

from geopy.geocoders import Nominatim

from pathlib import Path

# Create a dictionary to cache town/region combinations
cache = {}

def get_coordinates(town, region, country_code):
    key = f"{town} {region}"
    if not (town and region):
        return None
    elif key in cache:
        return cache[key]
    else:
        try:
            geolocator = Nominatim(user_agent="my_app")
            location = geolocator.geocode(key)

            if location:
                latitude = location.latitude
                longitude = location.longitude
                cache[key] = (latitude, longitude)
                return latitude, longitude
            else:
                return None
        except:
            print(f"Error in Geocoding for {town}, {region}")

# Example usage
directory = Path(__file__).parent.parent
bios = pd.read_csv(f'{directory}/clean-data/bios.csv')
bios['lat'] = None
bios['long'] = None

print("LENGTH", len(bios))

for index, row in bios.iterrows():
    info = bios.iloc[index]
    born_city, born_region, born_country = info[['born_city','born_region', 'born_country']].tolist()

    coordinates = get_coordinates(born_city, born_region, born_country)

    if coordinates:
        latitude, longitude = coordinates
        bios.loc[index, 'lat'] = latitude
        bios.loc[index, 'long'] = longitude
        # print(f"The coordinates of {born_city}, {born_region}, {born_country} are: Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("Unable to find coordinates for the specified location.")


    if index % 100 == 0:
        print(f"We're at {index}")

    if index % 1000 == 0:
        print(index)
        bios.to_csv(f'{directory}/checkpoints/bios_{index}.csv', index=False)





