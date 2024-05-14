import pandas as pd
TOTAL_FILES = 26

def location_helper(p):
    PATCH = p

    location_data = pd.read_csv('./bin/helpers/location'+PATCH+'.csv')

    # fetch only unique locations
    location_data = location_data.drop_duplicates(subset=['location_id'])

    # create new column of location_id which has patch number
    location_data['new_location_id'] = location_data['location_id'].apply(lambda x: PATCH+" " +str(x))

    # other important columns
    latitude = location_data['latitude']
    longitude = location_data['longitude']

    # concatenate the columns
    conc = pd.concat([location_data['new_location_id'], latitude, longitude], axis=1)

    # save the final data
    conc.to_csv('./bin/data/mock-location'+PATCH+'.csv',index=False)


for i in range(1,TOTAL_FILES+1):
    location_helper(str(i))

# merge all the data into one file
data = pd.read_csv('./bin/data/mock-location1.csv')
for i in range(2, TOTAL_FILES+1):
    data = data._append(pd.read_csv('./bin/data/mock-location'+str(i)+'.csv'))

data.to_csv('./bin/data/mocked-source-locations.csv',index=False)



# real location coordinates MERGER
data = pd.read_csv('archive/uk-train-stations.csv')

# run for loop to add 1 in every row of the column
data['new_location_id'] = 1
j = 0

for i in range(len(data)):
    if i % 100 == 0:
        j += 1
    data['new_location_id'][i] = str(j) + ' ' + str(i - (j-1)*100)




# other important columns
latitude = data['latitude']
longitude = data['longitude']
site = data['3alpha']
station_name = data['station_name']

# concatenate the columns
conc = pd.concat([data['new_location_id'], site, station_name, latitude, longitude], axis=1)

# save the final data
conc.to_csv('bin/real-location-coordinates.csv',index=False)

print('\n\n\ndone! with real location coordinates')