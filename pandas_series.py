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

letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))

# 1 Which letter occurs the most frequently in the letters Series?
 # letter y
letters.describe()['top']

# 2 Which letter occurs the Least frequently?
    #the least frequent letter is l
letters_count.idxmin()

# 3 How many vowels are in the Series?
    # there are 34 vowels
vowels =list('aeiou')
letters[letters.isin(vowels)].count()
#sum(letters.str.count(r'[aeiuo]'))

# 4 How many consonants are in the Series?
letters.str.len().count()
letters.str.len().count() - letters[letters.isin(vowels)].count()

# 5 Create a Series that has all of the same letters but uppercased.
uppercase_letters = letters.str.upper()
uppercase_letters

# 6 Create a bar plot of the frequencies of the 6 most commonly occuring letters.
letters_count.head(6)

letters_count.head(6).plot.bar()


# Use pandas to create a Series named numbers from the following list:
numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# 1 What is the data type of the numbers Series?
    # type object
numbers

# 2 How many elements are in the number Series?
    # There are 20 elements in the series
numbers.count()

# 3 Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers 
# Series to a numeric data type.
numbers.str.removeprefix("$")
numbers_2 = numbers.str.removeprefix("$").str.replace(',','').astype('float')

# 4 Run the code to discover the maximum value from the Series.
    # The maximum value is 4789988.17
numbers_2.max()

# 5 Run the code to discover the minimum value from the Series.
    # The minimum value is 278.6
numbers_2.min()

# 6 What is the range of the values in the Series?
    # the range is 4789709.57
numbers_2.max()-numbers_2.min()

# 7 Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.
'''
(-4511.11, 1197705.993]       7
(3592560.778, 4789988.17]     6
(1197705.993, 2395133.385]    4
(2395133.385, 3592560.778]    3
dtype: int64
'''

pd.cut(numbers_2,4).value_count

# 8 Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
pd.cut(numbers_2,4).value_counts().plot.bar(color='violet', width=.4)
plt.title('Numbers Value Counts 2 bins')
plt.xticks(rotation=45)
plt.xlabel('Numbers')
plt.ylabel('Frequency')
plt.show()