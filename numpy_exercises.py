import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1 How many negative numbers are there?
    there are 4 negative numbers
print(a[a < 0])
len(a[a<0])

# 2 How many positive numbers are there?
    # there are 5 negative numbers
print(a[a > 0])
len(a[a>0])

# 3 How many even positive numbers are there?
 # there are 3 positive numbers that are even
b = a[a>0]

b % 2 == 0

np.sum(b % 2 == 0)

# 4 If you were to add 3 to each data point, how many positive numbers would there be?
    # There are 10 positive numbers

b = a + 3

print (np.sum([b>0]))


# 5 If you squared each number, what would the new mean and standard deviation be?
    # the mean would be 74
    # the standard deviatio would be 144.0243035046516
np.square(a)
np.mean(np.square(a))
np.std(np.square(a))

# 6 A common statistical operation on a dataset is centering. 
#This means to adjust the data such that the mean of the data is 0. 
#This is done by subtracting the mean from each data point. 
(a -a.mean())


# 7 Calculate the z-score for each data point. Recall that the z-score is given by:
(a - a.mean())/a.std()


## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = np.array(a)


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a= min(a)
print (min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print (max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = (a).mean()
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in 
# the above list together
product_of_a = np.prod((a))
print(product_of_a)

# Exercise 6 - Make a variable named squares_of_a.
# It should hold each number in a squared like [1, 4, 9, 16, 25...]
squared_of_a = a**2
print (squared_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a[a% 2!= 0]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a[a% 2== 0]
print(evens_in_a)