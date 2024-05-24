# Weather Data Handler

This repository contains a tool to convert raw weather data from _OpenMateo_ into a format that can be easily imported into Power BI.

## Files

### A_Folders.py

- This script creates the folders needed to store the data in the correct format.

### B1_Weather_Helper.py

- This script contains the functions needed to **convert the raw data**.
- It works by separating **raw** `patch#.csv` file into clean `location#.csv` and `weather-data-no-location#.csv` files.

### B2_Location_Helper.py

- This script helps to **clean the location data**.
- There appeared to be an issue with the location coordinates, coming from _OpenMateo_, since it supported only the **first 2 decimal places**.
- This script fixes the issue by creating a **new file with the correct coordinates** from `uk-train-stations.csv`.

### B3_Mapper.py

- This script stitches **corrected-location** data to the **weather** data.
- So, it creates a final `FINAL-Weather.csv` file which then can be imported easily into **PowerBI**

### C_F-URL_Gen.py

- This script generates the **URLs** for the forecast raw data.
- It then creates a `FINAL-URLS.csv` file which contains the URLs for the forecast data.

### D_F_Download.py

- This script downloads the forecast data from the URLs in `FINAL-URLS.csv`.

### F1_Weather_Helper.py

- Works same as `B1_Weather_Helper.py` but for the forecast data.

### F2_Location_Helper.py

- Works same as `B2_Location_Helper.py` but for the forecast data.

### F3_Mapper.py

- Works same as `B3_Mapper.py` but for the forecast data.
