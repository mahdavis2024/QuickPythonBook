# Chapter 4 Try this 3
# TRY THIS: GETTING INPUT

city = input('Where do you live? ')
print('Welcome to %s.' %city)
dob = int(input('Which year were you born? '))
#today = input('What year is it? ')
today = int(input('What year is it? '))

age = today - dob
print('You are %s years old.' %age)

weight = float(input('your weight in kg? '))
height = float(input('your height in m? '))

BMI = weight/height**2
print('your BMI is: ',BMI)