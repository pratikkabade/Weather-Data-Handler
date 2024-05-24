import pandas as pd
import requests
import time

# Read the CSV file containing URLs
urls_df = pd.read_csv('data/FINAL-URLS.csv')

# Print the number of URLs opened
print('Forecast-URLs opened:', end=' ')

# Loop through each URL in the DataFrame
for index, row in urls_df.iterrows():
    # Get the URL
    url = row['URL']
    print(index + 1, end=' ')

    # Run this loop after 1 min to avoid the server blockage
    if (index + 1) % 5 == 0:
        print('\nSleeping for 1 minute...')
        time.sleep(65)
        print('...Continuing from :', end=' ')

    # Download the file from the URL
    response = requests.get(url)

    # Save the downloaded file
    file_name = f'archive/forecast-patch{index+1}.csv'
    with open(file_name, 'wb') as file:
        file.write(response.content)

print('\n')
print('Done with downloading files.')