import pandas as pd

# Read location data
location = pd.read_csv('bin/real-location-coordinates.csv')

# Extract latitude and longitude columns
lattitude = location['latitude'].rename('REAL_LAT')
longitude = location['longitude'].rename('REAL_LONG')

# Read weather data
weather = pd.read_csv('bin/weather-with-locations.csv')

# Merge weather_data and location_data based on 'new_location_id' and 'location_id'
merged_data = pd.merge(weather, location, left_on='location_id', right_on='new_location_id')

# Drop unnecessary columns
merged_data = merged_data.drop(columns=['new_location_id'])

# Rename the columns
merged_data = merged_data.rename(columns={'latitude_y':'REAL_LAT','longitude_y':'REAL_LONG'})

# Save the final data
merged_data.to_csv('data/FINAL-Weather.csv',index=False)

print('\n')
print('All done! Now download the file \n`data/FINAL-Weather.csv` \nand rename it to \n`Weather.csv`.')