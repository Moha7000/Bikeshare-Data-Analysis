# Project Name: 
US Bikeshare Data
____________________________________________________________________________________________________________________

# Project Overview: 
In this project, we will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.
____________________________________________________________________________________________________________________

# Bike Share Data
![image](https://user-images.githubusercontent.com/17765258/118907180-5ec49b80-b91f-11eb-8ce6-a828a5214ed9.jpg)
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, we will use data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. We will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.
____________________________________________________________________________________________________________________

# The Datasets:

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:
Gender
Birth Year
____________________________________________________________________________________________________________________

# Statistics Computed:

1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day

2 Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

3 Trip duration

total travel time
average travel time

4 User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)
____________________________________________________________________________________________________________________

# An Interactive Experience:

The experience is interactive because depending on a user's input to the following questions:

Would you like to see data for Chicago, New York, or Washington?
Would you like to filter the data by month, day, or not at all?
(If they chose month) Which month - January, February, March, April, May, or June?
(If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

