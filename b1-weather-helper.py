import pandas as pd
TOTAL_FILES = 26

def weather_helper(p):
    PATCH = p

    ### PART1 - Split the raw data in two different files ###
    # Open the file and find the blank line
    file1 = open('./archive/patch'+PATCH+'.csv', 'r')
    num = 0
    for line in file1:
        if line == '\n':
            break
        num += 1
    file1.close()

    # Read the first table from the file and save it
    location_data = pd.read_csv('./archive/patch'+PATCH+'.csv',nrows=num-1)
    location_data.to_csv('./bin/helpers/location'+PATCH+'.csv',index=False)

    # Read the second table from the file and save it
    data = pd.read_csv('./archive/patch'+PATCH+'.csv',skiprows=num+1)
    data.to_csv('./bin/helpers/weather-data-no-location'+PATCH+'.csv',index=False)





    ### PART2 - Focusing on both separated files one by one ###
    # Read the saved tables
    location_data = pd.read_csv('./bin/helpers/location'+PATCH+'.csv')
    weather_data = pd.read_csv('./bin/helpers/weather-data-no-location'+PATCH+'.csv')

    # Select 'time' column and process it
    time_data = weather_data['time']
    time_data = time_data.str.split('T').str[0]                     # Remove everything after 'T'
    time_data = time_data.groupby(time_data.index // 24).first()    # Merge 24 rows into 1 row

    # Calculate unique number of time
    unique_time = time_data.nunique()


    # Select and process columns from the data
    for i in range(2,len(weather_data.columns)):
        a = weather_data.columns[i]
        b = weather_data[a]
        b = b.groupby(b.index // 24).mean()
        time_data = pd.concat([ time_data, b], axis=1)
        
    # Get location_id from the data
    location = weather_data['location_id']
    location = location.groupby(location.index // 24).first()       # Merge 24 rows into 1 row


    # Get and process columns from location data
    latitude = location_data['latitude']
    longitude = location_data['longitude']
    new_location_id = location_data['location_id']

    # Repeat rows of latitude, longitude, and new_location_id based on unique_time
    latitude = latitude.repeat(unique_time)
    longitude = longitude.repeat(unique_time)
    new_location_id = new_location_id.repeat(unique_time)

    # Convert new_location_id to string and add patch number
    new_location_id = PATCH + ' ' + new_location_id.astype(str) 

    # Reset index for latitude, longitude, and new_location_id
    latitude = latitude.reset_index(drop=True)
    longitude = longitude.reset_index(drop=True)
    new_location_id = new_location_id.reset_index(drop=True)

    # Concatenate new_location_id, location, latitude, longitude
    location_data = pd.concat([new_location_id, location, latitude, longitude], axis=1)

    # Concatenate location_data and time
    final_data = pd.concat([location_data, time_data], axis=1)

    # Save the final data
    final_data.to_csv('./bin/data/weather-with-location'+PATCH+'.csv',index=False)

    print(PATCH, end=' ')

# Print the number of Patches Completed
print('Patches Completed:', end=' ')

# Call weather_helper for each file
for i in range(1, TOTAL_FILES+1):
    weather_helper(str(i))


# Merge all the data into one file
data = pd.read_csv('./bin/data/weather-with-location1.csv')
for i in range(2, TOTAL_FILES+1):
    data = data._append(pd.read_csv('./bin/data/weather-with-location'+str(i)+'.csv'))

# Save the merged data
data.to_csv('./bin/weather-with-locations.csv',index=False)

print('\n')
print('Done! Weather data is ready!')