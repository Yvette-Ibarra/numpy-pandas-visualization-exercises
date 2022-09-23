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
