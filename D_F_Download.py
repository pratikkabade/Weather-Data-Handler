import pandas as pd
import requests

# Read the CSV file containing URLs
urls_df = pd.read_csv('data/FINAL-URLS.csv')

# Print the number of URLs opened
print('Forecast-URLs opened:', end=' ')

# Loop through each URL in the DataFrame
for index, row in urls_df.iterrows():
    url = row['URL']
    print(index + 1, end=' ')

    # Download the file from the URL
    response = requests.get(url)

    # Save the downloaded file
    file_name = f'archive/forecast-patch{index+1}.csv'
    with open(file_name, 'wb') as file:
        file.write(response.content)

print('\n')
print('Done with downloading files.')