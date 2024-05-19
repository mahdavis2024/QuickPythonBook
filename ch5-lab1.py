'''
Lab 5: Examining a List
In this lab, the task is to read a set of temperature data (the monthly high temperatures
at Heathrow Airport for 1948 through 2016) from a file and then find some basic information:
 the highest and lowest temperatures, the mean (average) temperature,
and the median temperature (the temperature in the middle if all the temperatures are sorted).
The temperature data is in the file lab_05.txt in the source code directory for thischapter.
 Because I haven’t yet discussed reading files, here’s the code to read the files into a list:
temperatures = []
with open('lab_05.txt') as infile:
for row in infile:
temperatures.append(int(row.strip())
You should find the highest and lowest temperature, the average, and the median.
You’ll probably want to use the min(), max(), sum(), len(), and sort() functions/methods.
Bonus
Determine how many unique temperatures are in the list.
'''
temperatures = []
with open('lab_05.txt') as infile:
     for row in infile:
        temperatures.append(float(row.strip()))

min_temp = min(temperatures) 
max_temp = max(temperatures)
mean_temp = round(sum(temperatures)/len(temperatures), 2)
sorting = temperatures[:]
sorting.sort()
middle_index = len(temperatures)//2
median_temp = sorting[middle_index]

print('lowest temperatures: ', min_temp)
print('highest temperatures: ', max_temp)
print('mean/average temperatures: ', mean_temp)
print('median/middle temperatures: ', median_temp)
print('number of all temperatures: ', len(temperatures) )
unique = set(temperatures)
print('number of unique temperatures: ', len(unique))
