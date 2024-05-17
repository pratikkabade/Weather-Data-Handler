import pandas as pd
TOTAL_FILES = 26

def weather_helper(p):
    PATCH = p


    # get second table which is after blank line
    file1 = open('./archive/patch'+PATCH+'.csv', 'r')
    num = 0
    for line in file1:
        if line == '\n':
            break
        num += 1
    file1.close()

    # create 2 different files for the 2 tables
    # get first table which is from 2nd line
    location_data = pd.read_csv('./archive/patch'+PATCH+'.csv',nrows=num-1)
    # save the first table
    location_data.to_csv('./bin/helpers/location'+PATCH+'.csv',index=False)


    data = pd.read_csv('./archive/patch'+PATCH+'.csv',skiprows=num+1)
    # save the second table
    data.to_csv('./bin/helpers/weather-data-no-location'+PATCH+'.csv',index=False)












    # get second table which is from 5th line
    location_data = pd.read_csv('./bin/helpers/location'+PATCH+'.csv')
    data = pd.read_csv('./bin/helpers/weather-data-no-location'+PATCH+'.csv')

    # SELECTION OF COLUMN NAMES
    time = data['time']
    # remove everything after T
    time = time.str.split('T').str[0]
    # merge 24 rows into 1 row
    time = time.groupby(time.index // 24).first()

    # calculate unique number of time
    unique_time = time.nunique()


    # select columns from th data
    for i in range(2,len(data.columns)):
        a = data.columns[i]
        b = data[a]
        b = b.groupby(b.index // 24).mean()
        time = pd.concat([ time, b], axis=1)
        
    # get location_id from the data
    location = data['location_id']
    # elliminate 24 rows into 1 row
    location = location.groupby(location.index // 24).first()


    # from location data get the columns
    latitude = location_data['latitude']
    longitude = location_data['longitude']
    new_location_id = location_data['location_id']

    # show unique_times number of rows of latitude and longitude
    latitude = latitude.repeat(unique_time)
    longitude = longitude.repeat(unique_time)
    new_location_id = new_location_id.repeat(unique_time)

    # add patch number to each location_id
    new_location_id = PATCH + ' ' + new_location_id.astype(str) 

    # dont reindex on duplicate labels
    latitude = latitude.reset_index(drop=True)
    longitude = longitude.reset_index(drop=True)
    new_location_id = new_location_id.reset_index(drop=True)

    c = pd.concat([ new_location_id, location, latitude, longitude], axis=1)
    conc = pd.concat([c, time], axis=1)

    # save the final data
    conc.to_csv('./bin/data/weather-with-location'+PATCH+'.csv',index=False)

    print('patch'+PATCH+' done')


for i in range(1, TOTAL_FILES+1):
    weather_helper(str(i))


# merge all the data into one file
data = pd.read_csv('./bin/data/weather-with-location1.csv')
for i in range(2, TOTAL_FILES+1):
    data = data._append(pd.read_csv('./bin/data/weather-with-location'+str(i)+'.csv'))

data.to_csv('./bin/weather-with-locations.csv',index=False)

print('done! weather data is ready!')