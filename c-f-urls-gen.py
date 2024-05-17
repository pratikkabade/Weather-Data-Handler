import pandas as pd

location_coordinates = pd.read_csv('archive/uk-train-stations.csv')

# get columns from location
lattitude = location_coordinates['latitude']
longitude = location_coordinates['longitude']

# url-parts
base_url = 'https://api.open-meteo.com/v1/forecast?latitude='
post_url = '&daily=temperature_2m_max,wind_speed_10m_max&timezone=Europe%2FLondon&forecast_days=14&format=csv'

# urls array
urls = []

# create urls
print('rows-appended:',end=' ')
for i in range(len(lattitude)//100):
    url = base_url
    url2 = post_url
    
    for j in range(100):
        k = i*100 + j
        url += str(lattitude[k]) + ','
        # print('aaa',k)
    url = url[:-1] # remove last comma

    url += '&longitude='
    for j in range(100):
        k = i*100 + j
        url += str(longitude[k]) + ','
        # print('bbb',k)
    url = url[:-1] # remove last comma

    url += url2
    
    # add this url to a list
    urls.append(url)
    print((i+1)*100, end=' ')

print('\n')
print('\n')
print(len(urls))
# convert urls to a dataframe
urls_df = pd.DataFrame(urls)
urls_df.rename_axis("animal")

urls_df.to_csv('data/FINAL-URLS.csv',index=False)

print('\n' + 'done with url creation')