import pandas as pd

location_coordinates = pd.read_csv('archive/uk-train-stations.csv')

# get columns from location
lattitude = location_coordinates['latitude']
longitude = location_coordinates['longitude']

# url
url = 'https://api.open-meteo.com/v1/forecast?latitude='
post_url = '&daily=temperature_2m_max,wind_speed_10m_max&timezone=Europe%2FLondon&forecast_days=14&format=csv'

# urls array
urls = []

# create urls
print('rows appended',end=' ')
for i in range(len(lattitude)//100):
    for j in range(100):
        url += str(lattitude[j]) + ','
    url = url[:-1] # remove last comma

    url += '&longitude='
    for j in range(100):
        url += str(longitude[j]) + ','
    url = url[:-1] # remove last comma

    url += post_url
    
    # add this url to a list
    urls.append(url)
    print(i,end=' ')

# convert urls to a dataframe
urls_df = pd.DataFrame(urls)
urls_df.to_csv('data/FINAL-urls.csv',index=False)

print('\n' + 'done with url creation')