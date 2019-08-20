# HW08_AdvDataStore
## Surfs Up! Advanced-Data-Storage-and-Retrieval

![alt text](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/Img/surfs-up.png)

## Files
* [Data](https://github.com/DanielMJones2005/HW08_AdvDataStore/tree/master/Data)
    * hawaii.sqlite
    * hawaii_measurements.csv
    * hawaii_stations.csv
 
 * [Dev_PythonFiles](https://github.com/DanielMJones2005/HW08_AdvDataStore/tree/master/Dev_PythonFiles)
    * climate_dev.v1.ipynb
    * climate_dev.v2.ipynb
    * climate_dev.v3.ipynb
    * climate_starter.ipynb
    * routes_dev.v1.py
 
  * [Img](https://github.com/DanielMJones2005/HW08_AdvDataStore/tree/master/Img)
    * Relevant image files:
    * hw.Dec_tobs_Box.png
    * hw.June_tobs_Box.png
    * hw.TripAvgTemp.png
    * hw.dailynormals.png
    * hw.prcp.png
    * hw.tobs.png
    * surfs-up.png
  
  * [.gitignore](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/.gitignore)
  * [climate_master.ipynb](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/climate_master.ipynb)
  * [routes_master.py](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/routes_master.py)
  
  ## Step 1 - Climate Analysis and Exploration
  - Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.
  - Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.
      - Trip Dates:
            - start_date = "2018-06-01"
            - end_date = "2018-06-15"
       - Prior Year Dates:
            - start_date = "2017-06-01"
            - end_date = "2017-06-15"
  - Use SQLAlchemy create_engine to connect to your sqlite database.
  - Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement
   
   ## Precipitation Analysis
   - Design a query to retrieve the last 12 months of precipitation data.
   - Select only the date and prcp values.
   - Load the query results into a Pandas DataFrame and set the index to the date column.
   - Sort the DataFrame values by date.
   - Plot the results using the DataFrame plot method
   ![alt text](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/Img/hw.prcp.png)
   
   ## Station Analysis
   - Design a query to calculate the total number of stations.
        - Total # Stations: 9
   - Design a query to find the most active stations.
   - List the stations and observation counts in descending order.
   - Which station has the highest number of observations?
        - Station: USC00519281, 2772 Observations
   - Design a query to retrieve the last 12 months of temperature observation data (tobs).
        - Filter by the station with the highest number of observations.
        - Plot the results as a histogram with bins=12.  
    ![alt text](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/Img/hw.tobs.png)   
    
    ## Step 2 - Climate App
    - See [routes_dev.v1.py](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/routes_master.py)
    * /
      ** Home page.
      ** List all routes that are available.
    * /api/v1.0/precipitation
      ** Convert the query results to a Dictionary using date as the key and prcp as the value.
      ** Return the JSON representation of your dictionary.
  * /api/v1.0/stations
      ** Return a JSON list of stations from the dataset.
  * /api/v1.0/tobs
      ** query for the dates and temperature observations from a year from the last data point.
      ** Return a JSON list of Temperature Observations (tobs) for the previous year.
  * /api/v1.0/<start> and /api/v1.0/<start>/<end>
      ** Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
      ** When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
      ** When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
      
  ## Optional: Other Recommended Analyses
  
  ## Temperature Analysis I
  - Hawaii is reputed to enjoy mild weather all year. 
  - Is there a meaningful difference between the temperature in, for example, June and December?
      - Yes, there is a meaningful difference between the temperature in June vs December.
         ![alt text](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/Img/hw.June_tobs_Box.png)  
         ![alt text](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/Img/hw.Dec_tobs_Box.png)
      
  - Identify the average temperature in June at all stations across all available years in the dataset. 
  - Do the same for December temperature.
  - Use the t-test to determine whether the difference in the means, if any, is statistically significant. 
      - Will you use a paired t-test, or an unpaired t-test? Why?
          - An unpaired t-test because the two population have different number of samples
          - If the p value is less than 0.05, you reject the null hypothesis, and say that you find a significant difference
          - P-Value of 4.193529835915755e-187
          - June tobs vs Dec tobs: The differences between some of the means are statistically significant  
  
  ## Temperature Analysis II
  - The starter notebook contains a function called calc_temps that will accept a start date and end date in the format %Y-%m-%d and return the minimum, average, and maximum temperatures for that range of dates.
  - Use the calc_temps function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").
  - Plot the min, avg, and max temperature from your previous query as a bar chart.
      - Use the average temperature as the bar height.
      - Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr).
      ![alt text](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/Img/hw.TripAvgTemp.png)
     
   - Calculate the total amount of rainfall per weather station for your trip dates using the previous year's matching dates.
   - Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation 
  
  ## Daily Rainfall Average
  - Calculate the rainfall per weather station using the previous year's matching dates.
  - Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.
  - You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic tobs that match that date string.
  - Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.
  - Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.
  - Use Pandas to plot an area plot (stacked=False) for the daily normals.
      ![alt text](https://github.com/DanielMJones2005/HW08_AdvDataStore/blob/master/Img/hw.dailynormals.png)
