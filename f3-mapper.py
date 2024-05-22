import pandas as pd

# Read location data
location = pd.read_csv('bin/forecast-real-location-coordinates.csv')

# Extract latitude and longitude columns
lattitude = location['latitude'].rename('REAL_LAT')
longitude = location['longitude'].rename('REAL_LONG')

# Read weather data
weather = pd.read_csv('bin/forecast-weather-with-locations.csv')

# Merge weather_data and location_data based on 'new_location_id' and 'location_id'
merged = pd.merge(weather, location, left_on='location_id', right_on='new_location_id')

# Drop unnecessary columns
merged = merged.drop(columns=['new_location_id'])

# Rename the columns
merged = merged.rename(columns={'latitude_y':'REAL_LAT','longitude_y':'REAL_LONG'})

# Save the final data
merged.to_csv('data/FINAL-Forecast-Weather.csv',index=False)

print('\n')
print('All done! Now download the file \n`data/FINAL-forecast-Weather.csv` \nand rename it to \n`Forecast-Weather.csv`.')