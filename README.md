# My-Project

Weather Data Analysis Project
Project Overview
This project involves the analysis and visualization of weather data, including rainfall, temperature, and wind speed. The dataset contains records of several weather parameters over time. Using Python, the data is plotted to provide clear and comprehensive insights into different weather trends.

The Python script automates the process of reading the dataset, handling the data, and generating visual representations in the form of line plots. These visualizations help in understanding patterns in rainfall, temperature fluctuations, and wind speed over time.

Data Description
The dataset used for this project includes the following columns:

Date: The date of the recorded weather data.
Highest 120 min Rainfall (mm): The highest recorded rainfall over a 120-minute period.
Highest 60 min Rainfall (mm): The highest recorded rainfall over a 60-minute period.
Highest 30 min Rainfall (mm): The highest recorded rainfall over a 30-minute period.
Maximum Temperature (°C): The highest temperature recorded on a given date.
Minimum Temperature (°C): The lowest temperature recorded on a given date.
Mean Temperature (°C): The average temperature recorded on a given date.
Mean Wind Speed (km/h): The average wind speed on a given date.
Max Wind Speed (km/h): The highest wind speed recorded on a given date.
Visualization
Using Python’s matplotlib library, multiple line plots are generated to visualize the trends in the dataset. The weather parameters are plotted over time (dates), showing:

Rainfall Data: Highest rainfall values recorded over 30, 60, and 120-minute periods.
Temperature Data: Maximum, minimum, and mean temperature values.
Wind Speed Data: Mean and maximum wind speeds.
The visualizations are presented in both combined and separate formats:

Combined Plot: All weather parameters are plotted in a single figure to provide an overview.
Subplots: Rainfall, temperature, and wind speed are shown in individual subplots for clearer insights into each category.


How to Use
1.Clone the Repository:
  	git clone <repo-url>
  	cd weather-data-analysis
2.Install Required Libraries: Make sure you have the required Python libraries installed by running:
	pip install -r requirements.txt
3.Run the Script: Execute the Python script to generate the plots
	python plot_weather_data.py


Conclusion
This project demonstrates how Python can be used to automate the process of analyzing large weather datasets and generating meaningful visualizations. The ability to quickly visualize data trends can be highly beneficial in the fields of meteorology, environmental research, and engineering


