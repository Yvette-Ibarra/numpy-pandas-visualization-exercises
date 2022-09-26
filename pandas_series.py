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
    # type "O" for object
fruits.dtype
#type(fruits)

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
# fruits.value_counts().tail(11)

# Alternative code
fruits.value_counts().nsmallest(n=1, keep = 'all')
# Exercises Part II

# Explore more attributes and methods while you continue to work with the fruits Series.

# 1 Capitalize all the string values in fruits.
# fruits.str.upper()
 
 # Alternative code capitalize only the first letter
fruits.str.capitalize()

# fancy code
fruits.apply(lambda x: x + 'count of a:' + str(x.count('a')))


# 2 Count the letter "a" in all the string values (use string vectorization).

fruits.str.count('a')
#sum(fruits.str.count('a'))

# 3 Output the number of vowels in each and every string value.

fruits.str.lower().str.count(r'[aeiou]')
# fruits.str.count('a|e|i|o|u')

# Fancy Code
# list comprehension with function
def count_vowels(word):
    return len([let for let in word.lower() if let in vowels])
fruits.apply(count_vowels)

# 4 Write the code to get the longest string value from fruits.
fruits[fruits.str.len()== fruits.str.len().max()]

# alternative code with variable for mask
bool_mask = fruits.str.len() == fruits.str.len().max()
fruits[bool_mask]

# 5 Write the code to get the string values with 5 or more letters in the name.
#fruits[(fruits.str.len().max())>= 5
fruits[fruits.str.len()>=5]

#6 Find the fruit(s) containing the letter "o" two or more times.
fruits[fruits.str.count('o')>=2]

# 7 Write the code to get only the string values containing the substring "berry".
fruits[fruits.str.contains('berry')]

# alternative code using lambda function
fruits[fruits.apply(lambda x: 'berry' in x)]

# 8 Write the code to get only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]

# alternative code using mask
bool_mask = fruits.str.contains('apple')
fruits[bool_mask]

# 9 Which string value contains the most vowels?
fruits[fruits.str.count('a|e|i|o|u') == fruits.str.count('a|e|i|o|u').max()]

# altrnative code using cout_vowels function
#fruits.apply(count_vowels).max()
new_mask = fruits.apply(count_vowels) ==fruits.apply(count_vowels).max()
fruits[new_mask]


# Exercises Part III

# Use pandas to create a Series named letters from the following string. The easiest way to make this string into a Pandas series is to use list to convert each individual letter into a single string on a basic Python list.

letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))

# 1 Which letter occurs the most frequently in the letters Series?
 # letter y
letters.describe()['top']

# 2 Which letter occurs the Least frequently?
    #the least frequent letter is l
letters_count.idxmin()


# alternative code using nsmallest 
letters.value_counts().nsmallest(n=1, keep='all')

# 3 How many vowels are in the Series?
    # there are 34 vowels
vowels =list('aeiou')
letters[letters.isin(vowels)].count()
#sum(letters.str.count(r'[aeiuo]'))

# 4 How many consonants are in the Series?
letters.str.len().count()
letters.str.len().count() - letters[letters.isin(vowels)].count()

# alternative code using is_vowel function
    # 34
def is_vowel(some_word):
    return some_word in ['a','e','i','o','u']
letters.str.lower().apply(is_vowel).sum()

# 5 Create a Series that has all of the same letters but uppercased.
    # 166
uppercase_letters = letters.str.upper()
uppercase_letters

# alternative code using ~ to negate a statement
~letters.str.lower().apply(is_vowel)
(~letters.str.lower().apply(is_vowel)).sum()


# 6 Create a bar plot of the frequencies of the 6 most commonly occuring letters.
letters_count.head(6)

letters_count.head(6).plot.bar()

# Alternative code turn to horizontal bar plot
letters.value_counts().head(6).plot(kind ='barh')
plt.title('top six all time letters')
plt.show()

# Use pandas to create a Series named numbers from the following list:
numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# 1 What is the data type of the numbers Series?
    # type object
numbers

# 2 How many elements are in the number Series?
    # There are 20 elements in the series
numbers.count()
# alternative code
numbers.nunique()

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

# plot that is vertical histogram

pd.cut(numbers,4).value_counts().sort_index().plot(kind='barh')
plt.title('4 bins')
plt.xlabel('count')
plt.ylabel('bins')
# Use pandas to create a Series named exam_scores from the following list:
exam_score = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
)

# 1 How many elements are in the exam_scores Series?
    # there are 20 elements
exam_score.count()

# 2 Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.
    # max is 96 , min is 60, meidan is 79
exam_score.describe()
exam_score.median()

# 3 Plot the Series in a meaningful way and make sure your chart has a title and axis labels.
exam_score.plot.bar(color = 'orange', width = .5)
plt.title('Exam Scores')
plt.xticks(rotation = 0)
plt.xlabel('student id')
plt.ylabel('Score')

plt.show()

# 4 Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades.
# Add the necessary points to the highest grade to make it 100, and add the same number of points to every 
# other score in the Series as well.

add_points = 100-exam_score.max()
curved_grades = exam_score + add_points
curved_grades

# 5 Use a method to convert each of the numeric values in the curved_grades
# Series into a categorical value of letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. 
# Save this as a Series named letter_grades.

def get_letter_grade (number):
    if number >= 90:
        return ('A')
    elif number >= 80:
        return('B')
    elif number >= 67:
        return('C')
    else:
        return('F')

letter_grades = curved_grades.apply(get_letter_grade)
letter_grades


# Alternative Code using bins and defining bin edges
bin_edges = [0, 70, 75, 80, 90, 100]
bin_labels = ['F', 'D', 'C', 'B', 'A']
letter_grades = pd.cut(curved_grades, bins = bin_edges, labels= bin_labels)

letter_grades

# 6 Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.
letter_grades.value_counts().plot.bar(color = 'blue', width = .8)
plt.title('Letter Grade Count')
plt.xticks(rotation=15)
plt.xlabel('Letter')
plt.ylabel('count')

plt.show()

# Alternative code using horizontal bar graph
letter_grades.value_counts().sort_index().plot.barh()
plt.title('Letter grades Distribution')
plt.show()