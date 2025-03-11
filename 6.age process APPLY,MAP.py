import pandas as pd
from functools import reduce
# Sample data (age of people in a list)
ages = [15, 22, 19, 35, 40, 60, 55, 30, 65, 72, 80]
# 1. Using `apply()` with pandas to categorize people into age groups (Child, Adult, Senior)
df = pd.DataFrame({'Age': ages})
def categorize_age(age):
if age < 18:
return 'Child'
elif 18 <= age <= 65:
return 'Adult'
else:
return 'Senior'
df['Age Group'] = df['Age'].apply(categorize_age)
print("DataFrame after applying categorize_age function:")
print(df)
# 2. Using `filter()` to filter out ages that are less than 18 (child ages)
children_ages = list(filter(lambda age: age < 18, ages))
print("\nAges of children:")
print(children_ages)
# 3. Using `map()` to increase everyone's age by 1 year (for the next birthday)
next_birthday_ages = list(map(lambda age: age + 1, ages))
print("\nAges after increasing by 1 (next birthday):")
print(next_birthday_ages)
# 4. Using `reduce()` to find the total sum of all ages
total_age = reduce(lambda x, y: x + y, ages)
print("\nTotal sum of all ages:")
print(total_age)
# 5. Optional: Using reduce to find the average age by dividing the total sum by the number of people
average_age = total_age / len(ages)
print("\nAverage age of all people:")
print(average_age)