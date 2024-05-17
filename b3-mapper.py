import pandas as pd

# read bin/real-location-coordinates.csv
location = pd.read_csv('bin/real-location-coordinates.csv')

# get columns from location
lattitude = location['latitude']
longitude = location['longitude']

# read bin/weather-with-locations.csv
weather = pd.read_csv('bin/weather-with-locations.csv')


# change header of lattitude and longitude
lattitude = lattitude.rename('REAL_LAT')
longitude = longitude.rename('REAL_LONG')


# merge based on new_location_id from location and location_id from weather
merged = pd.merge(weather, location, left_on='location_id', right_on='new_location_id')

# now drop the columns that are not needed
merged = merged.drop(columns=['new_location_id'])

# rename the columns
merged = merged.rename(columns={'latitude_y':'REAL_LAT','longitude_y':'REAL_LONG'})


# save the final data
merged.to_csv('data/FINAL-Weather.csv',index=False)

print('all done! \n\n\nnow download the file `data/FINAL-Weather.csv` and rename it to `Weather.csv`')
