import pandas as pd

# Read location coordinates
location_coordinates = pd.read_csv('archive/uk-train-stations.csv')

# Extract latitude and longitude columns
lattitude = location_coordinates['latitude']
longitude = location_coordinates['longitude']

# Define base and post URL parts
base_url = 'https://api.open-meteo.com/v1/forecast?latitude='
post_url = '&daily=temperature_2m_max,wind_speed_10m_max&timezone=Europe%2FLondon&forecast_days=14&format=csv'

# Initialize URLs list
urls = []

# Print progress
print('Rows appended:', end=' ')

# Generate URLs
for i in range(len(lattitude)//100):
    url = base_url
    url2 = post_url
    
    for j in range(100):
        k = i*100 + j
        url += str(lattitude[k]) + ','
    url = url[:-1] # remove last comma

    url += '&longitude='
    for j in range(100):
        k = i*100 + j
        url += str(longitude[k]) + ','
    url = url[:-1] # remove last comma

    url += url2
    
    # Add the generated URL to the list
    urls.append(url)

    # Print progress
    print((i+1)*100, end=' ')


# Print the number of URLs
print(f'\n\nNumber of URLs: {len(urls)}\n')

# Convert URLs list to a DataFrame
urls_df = pd.DataFrame(urls, columns=['URL'])

# Save the DataFrame to a CSV file
urls_df.to_csv('data/FINAL-URLS.csv', index=False)

print('Done with URL creation.')