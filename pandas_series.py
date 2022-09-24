#Exercises Part I

#Make a file named pandas_series.py or pandas_series.ipynb for the following exercises.

#Use pandas to create a Series named fruits from the following list:


#    ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
#Use Series attributes and methods to explore your fruits Series.

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# 1 Determine the number of elements in fruits.
    # there are 17 elements in fruits
fruits.count()

# 2 Output only the index from fruits.
    #RangeIndex(start=0, stop=17, step=1)
fruits.index

# 3 Output only the values from fruits.
fruits.values

# 4 Confirm the data type of the values in fruits.
    # pandas.core.series.Series
type(fruits)

# 5 Output only the first five values from fruits. Output the last three values. 
# Output two random values from fruits.
fruits.head()
fruits.tail(3)
fruits.sample(2)

# 6 Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()

# 7 Run the code necessary to produce only the unique string values from fruits.
fruits.unique()

# 8 Determine how many times each unique string value occurs in fruits.
fruits.value_counts()

# 9 Determine the string value that occurs most frequently in fruits.
    # kiwi
fruits.describe()['top']
fruits.value_counts().head(1)

# 10 Determine the string value that occurs least frequently in fruits.
fruits
fruits.value_counts().tail(11)

# Exercises Part II

# Explore more attributes and methods while you continue to work with the fruits Series.

# 1 Capitalize all the string values in fruits.
fruits.str.upper()

# 2 Count the letter "a" in all the string values (use string vectorization).

fruits.str.count('a')
#sum(fruits.str.count('a'))

# 3 Output the number of vowels in each and every string value.

fruits.str.lower().str.count(r'[aeiou]')
# fruits.str.count('a|e|i|o|u')

# 4 Write the code to get the longest string value from fruits.
fruits[fruits.str.len()== fruits.str.len().max()]

# 5 Write the code to get the string values with 5 or more letters in the name.
#fruits[(fruits.str.len().max())>= 5
fruits[fruits.str.len()>=5]

#6 Find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.str.count('o')>=2]

# 7 Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]

# 8 Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]

# 9 Which string value contains the most vowels?
fruits[fruits.str.count('a|e|i|o|u') == fruits.str.count('a|e|i|o|u').max()]


# Exercises Part III

# Use pandas to create a Series named letters from the following string. The easiest way to make this string into a Pandas series is to use list to convert each individual letter into a single string on a basic Python list.





