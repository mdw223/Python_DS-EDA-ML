Lectures 10-11

# Data Science definition

"Data Science is a multidisciplinary field of study that combines programming skills, domain expertise and knowledge of statistics and mathematics to extract useful insights and knowledge from data". Those who practice data science are called "data scientists". They combine a wide range of skills and modern technologies to analyze data collected from sensors, customers, smartphones, the web, and other sources.
[Source](https://towardsdatascience.com/data-science-101-life-cycle-of-a-data-science-project-86cbc4a2f7f0/)

# Data Science life cycle

1. Understanding the Business problem
2. Data collection
3. data cleaning and processing
4. EDA (exploratory data analysis)
5. model building and evaluation
6. communicating model result
7. model deploy and maintainance


# Numpy ndarrays

ndarray is a flexible container for numerical data of a uniform type, an extension of the Python array module 

## creation

arr = np.array([1,2,3])

It can take a list, tuple, a list of lists of equal length.

Can also generate a random array

np.random.rand(3,2) 

This creates a random array of 3 rows, 2 columns.

np.zeros(8)  np.ones(3)

This creates an array of zeros or ones

arr = np.zeros((3, 4))
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]   

np.one_like(arr1) 

can create an array of ones like the shape of the one passed

np.arange(2, 16, 3)

this is like the range function 

you can specify its data type upon creation too

np.array([5.6, 10.2], dtype = np.float64)

arr4.dtype 

you can print that to get the data type.

arr4.shape

to get its shape

can cast its data type

arr4.astype(np.int32)

## indexing

can index like scores[-1][2] and x[10]

## slicing

can do array[start:stop:step] 

For example, to get the last element in each Row of a 2D array 

arr[:,-1]



A deep copy of an object is a copy whose properties do not share the same references (point to the same underlying values).

Slicing a list produces a sublist that is deep copy. 

Numpy array slices still reference the original copy.

So to produce a deep copy, use .copy()

two = np.array([[10,20,30],[40,50,60], [70, 80, 90],[100,110,120]])

s6 = two[2:, 1:2] 

Starts at the 2nd index in the array, and gets the 1 index in those subarrays.

produces:

[ [80]
  [110] ]

## arithmetic ops

can do:
+ or np.add
- or np.subtract or np.negative
np.floor_divide or //
ect

so you can do arr3 = arr1 + arr2 or arr3=np.add(arr1, arr2)

comparison like com = arr2 > arr3
[[False,  True], 
 [False, False], 
 [False, False]] 


------

# Pandas series

Series – a fixed-length ordered dictionary, a mapping of index values to data values (an array plus an index). where by default the index (on left) will consist of integers 0 through len – 1. 

## creation

obj1 = pd.Series([4, 7, -1, 2])
0    4 
1    7 
2   -1 
3    2 
dtype: int64

obj1.values
    array([ 4,  7, -1,  2])
use to view the array representation of the series

Can create a Series from a dict:
canines = {"Spot": 9.2, "Lassie":24.5, "Fido": 102.1} 
dogs = pd.Series(canines) 

CAN ADD AN INDEX VIA:
dogs.name = 'weight' 
dogs.index.name = 'petname' 
dogs

petname 
Spot        9.2 
Lassie     24.5 
Fido      102.1 
Name: weight, dtype: float64 

## indexing 

to view the index
obj1.index 
    RangeIndex(start=0, stop=4, step=1) 

can specify the index
pd.Series([4, 7, -1, 2], index = ['x', 'y', 'z', 't']) 

## Selecting 

You can index a Series using the array index or the array label
obj2[2] 
-1 
obj2['z'] 
-1 

## slicing and subsetting

obj2[0:2] 
 
x    4 
y    7 
dtype: int64

obj2['x':'z'] 
 
x    4 
y    7 
z   -1 
dtype: int64 

IF THE INDEXES ARE NOT IN ORDER FOR FULL:
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5]) 
1    a 
3    b 
5    c 
dtype: object 

data[1] 
'a'

data[1:3] 
 
3    b 
5    c 
dtype: object 

*** THIS IS EXPLICIT SLICING. Uses the explicit index.

In Pandas, .loc[] uses explicit slicing

data.loc[1] 
'a' 
 
data.loc[1:3] 
 
1    a 
3    b 
dtype: object 

.iloc[] is implicit, so it will treat the index as its actual position in the series, not its indexes' number

data.iloc[1] 
'b' 
 
data.iloc[1:3] 
 
3    b 
5    c 
dtype: object

## Operations

obj2[obj2 > 2]   # masking

't' in obj2     # boolean

------

# Pandas Dataframes

DataFrame – a rectangular table of data, an ordered collection of columns of various types, has both a row and  a column index, a dictionary of aligned Series (share the same index) but stored as 1- and 2-dimensional array blocks.

## CREATION

dict = {'petname': ['Spot', 'Lassie']
        'months:   [4, 10]
        }
df = pd.DataFrame(dict)

Can specify the columns and indexes during creation like:
import numpy as np 
newdf = pd.DataFrame(np.random.randn(3,2), columns = ['yes', 'no'],   index = ['yesterday', 'today', 'tomorrow']) 


## VIEW 

USE df.head() to view the first 5 rows (or df.tail() to view the last 5 rows) 

VIEW COLUMNS
df.columns 
    Index(['petname', 'months', 'weight', 'heartworm', 'vac', 'fleas'], dtype='object')

## SELECT

you can retrieve a column as a Series either by dict notation or by attribute.

df['petname']   or  df.petname 

0      Spot 
1      Spot 
2      Spot 
3    Lassie 
4    Lassie 
5    Lassie 
6      Fido 
7      Fido 
8      Fido 
Name: petname, dtype: object 
 
THis is the series of that column.

GETTING A SUBSET based on specifying the columns

df[['petname', 'vac', 'heartworm']] 

We can also do based on index:

df.loc[2]    or   df.iloc[2]

df.loc[[2,4]]  or   df.iloc[[2,4]] 

We can subset a row based upon a Boolean expression: 
df[df['months'] >= 18] 

Or by slicing:
df[2:4] 

We can subset based upon a list:
df[df['petname'].isin(["Spot","Fido"])]

## Manipulating

Add a column via:

df['heartworm'] = True # fills true for each row in the column

Can Add a new column where we specify the values for each row in the column:

rabies = pd.Series(["True", "True", "False", "True", "True", "False"], index =[0,1,2,6,7,8])
df["vac"] = rabies 


DELETE A COLUMN
del df['fleas']
