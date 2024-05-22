import pandas as pd
TOTAL_FILES = 26

def location_helper(p):
    PATCH = p

    # Read location data
    location_data = pd.read_csv('./bin/helpers/location'+PATCH+'.csv')

    # Fetch only unique locations
    location_data = location_data.drop_duplicates(subset=['location_id'])

    # Create new column of location_id which has patch number
    location_data['new_location_id'] = location_data['location_id'].apply(lambda x: PATCH+" " +str(x))

    # Other important columns
    latitude = location_data['latitude']
    longitude = location_data['longitude']

    # Concatenate the columns
    conc = pd.concat([location_data['new_location_id'], latitude, longitude], axis=1)

    # Save the final data
    conc.to_csv('./bin/data/mock-location'+PATCH+'.csv',index=False)


# Call location_helper for each file
for i in range(1,TOTAL_FILES+1):
    location_helper(str(i))

# Merge all the data into one file
data = pd.read_csv('./bin/data/mock-location1.csv')
for i in range(2, TOTAL_FILES+1):
    data = data._append(pd.read_csv('./bin/data/mock-location'+str(i)+'.csv'))

# Save the merged data
data.to_csv('./bin/data/mocked-source-locations.csv',index=False)



# Real location coordinates MERGER
data = pd.read_csv('archive/uk-train-stations.csv')

# Initialize 'new_location_id' column with 1
data['new_location_id'] = 1
counter = 0

# Update 'new_location_id' for each row
for i in range(len(data)):
    if i % 100 == 0:
        counter += 1
    data['new_location_id'][i] = str(counter) + ' ' + str(i - (counter-1)*100)




# Select important columns
latitude = data['latitude']
longitude = data['longitude']
site = data['3alpha']
station_name = data['station_name']

# Concatenate the columns
concatenated_data = pd.concat([data['new_location_id'], site, station_name, latitude, longitude], axis=1)

# Save the final data
concatenated_data.to_csv('bin/real-location-coordinates.csv',index=False)

print('\n')
print('Done with real location coordinates.')