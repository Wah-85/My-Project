import pandas as pd
import matplotlib.pyplot as plt


# Read data from CSV file
df=pd.read_csv("C:\\Users\\wah wah\\Desktop\\Exercises Python\\DAILYDATA_S24_202408.csv")
print(df)

# Create subplots: 3 rows, 1 column
fig, axs = plt.subplots(3, 1, figsize=(10, 15), sharex=True)

# Plotting Rainfall Data in the first subplot
axs[0].plot(df['Date'], df['Highest 120 min Rainfall (mm)'], label='Highest 120 min Rainfall (mm)', color='r', marker='.', ls='-')
axs[0].plot(df['Date'], df['Highest 60 min Rainfall (mm)'], label='Highest 60 min Rainfall (mm)', color='b', marker='x')
axs[0].plot(df['Date'], df['Highest 30 min Rainfall (mm)'], label='Highest 30 min Rainfall (mm)', color='g', marker='o')
axs[0].set_title('Rainfall Data')
axs[0].set_ylabel('Rainfall (mm)')
axs[0].legend()
axs[0].grid()

# Plotting Temperature Data in the second subplot
axs[1].plot(df['Date'], df['Maximum Temperature (°C)'], label='Maximum Temperature (°C)', color='y', marker='v', ls='--')
axs[1].plot(df['Date'], df['Minimum Temperature (°C)'], label='Minimum Temperature (°C)', color='m', marker='.')
axs[1].plot(df['Date'], df['Mean Temperature (°C)'], label='Mean Temperature (°C)', color='g', marker='v', ls=':')
axs[1].set_title('Temperature Data')
axs[1].set_ylabel('Temperature (°C)')
axs[1].legend()
axs[1].grid()

# Plotting Wind Speed Data in the third subplot
axs[2].plot(df['Date'], df['Mean Wind Speed (km/h)'], label='Mean Wind Speed (km/h)', color='k', marker='^')
axs[2].plot(df['Date'], df['Max Wind Speed (km/h)'], label='Max Wind Speed (km/h)', color='r', marker='.', lw=2)
axs[2].set_title('Wind Speed Data')
axs[2].set_ylabel('Wind Speed (km/h)')
axs[2].legend()
axs[2].grid()

# Set x-axis label for the bottom subplot
axs[2].set_xlabel('Date')
#plt.gcf().autofmt_xdate()

# Adjust layout for better spacing
#plt.tight_layout()

# Show the plot
plt.show()
