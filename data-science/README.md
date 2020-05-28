- [Python for Beginners](#Python-for-Beginners)
- [Pandas](#Pandas)

# Python for Beginners

## Elementary Stuff

```python
print(2 ** 3) # this is 2^4

multi_line_string = """
Hello Whatsup
Yo bro chillin??
"""								

print("hello", end="") # next line not initiated

# Functions and parameters
def foo(title, row_count):
  print(title, end="")
  print(" "+ str(row_count))
	return 20, 'hello'
val, string_returned = create_spreadsheet("Alapan", 10)
```

## Errors and Others

```python
def divide_two_numbers(x, y):
  result = x / y
  return result

try:
  result = divide_two_numbers(2,0)
  print(result)
except NameError:
  print("A NameError occurred.")
except ValueError:
  print("A ValueError occurred.") 
except ZeroDivisionError:
  print("A ZeroDivisionError occurred.")
```

## Conditions

```python
def simple_conditional(x):
  if x == 0:
    print("x is equal to zero.")
  elif x > 0:
    print("x is greater than zero.")
  else:
    print("x is less than zero.")

simple_conditional(0)
```

## Lists

```python
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]

names_and_heights = zip(names, heights)
print(list(names_and_heights))

new_orders = orders + ['lilac', 'rose']
new_orders.append('iris')
i = new_orders.pop()

list1 = range(1, 8, 2) # equivalent to [1, 3, 5, 7]
print(list(list1))

print(len(my_list))

sublist = letters[1:6]
num_i = letters.count('i')

names.sort()
sorted_names = sorted(names)

my_info = ('Alapan', 19, 5.0)
name, age, version = my_info
```

## Loops

```python
# jump statements
break
continue

# loops
for i in students:
	---------------

for i in range(0, 50, 3):
	---------------

while <condition>:
	---------------

# list comprehension
new_collection = [word for word in collection if word[-1] == 'z']
numbers = [i + 10 for i in values if i > 0]

nested_lists = [[4, 8], [16, 15], [23, 42]] # given
greater_than = [i > j for (i,j) in nested_lists]

quotients = [j/i for (i,j) in list(zip(a, b))]
```

## Lambda

```python
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A...'

random.randint(a,b) # will return an integer between a and b (inclusive)
```

# Pandas

## Introduction

```python
import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(df1)

df2 = pd.DataFrame([
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ],
    columns=['name', 'address', 'age'])
```

## CSV

```python
df = pd.read_csv('my-csv-file.csv')
df.to_csv('new-csv-file.csv')

clinic_north = df.clinic_north # select column
print(type(clinic_north))
print(type(df))

clinic_north_south = df[['clinic_north', 'clinic_south']] # select multiple columns

march = df.iloc[2] # select row 2 zero-indexed
april_may_june = df.iloc[-3:]
example = orders.iloc[1:4]

df2 = df.loc[[1, 3, 5]]

january = df[df.month == 'January'] # checking-based most
# most logical ('|' as 'or' and & as 'and') and relational (<, !=, etc) operators allowed
march_april = df[(df.month == 'March') | (df.month == 'April')]

january_february_march = df[df.month.isin(['January', 'February', 'March'])]

df3 = df2.reset_index(drop = True, inplace = True)
```

## Manipulations

```python
# Adding new columns 
df['Is taxed?'] = 'Yes' # is same as 
df['Is taxed?'] = ['Yes', 'Yes', 'Yes'] # consider presence of three rows in data set

df['Lowercase Name'] = df.Name.apply(lower)

get_last_name = lambda x: x.split()[-1]
df['last_name'] = df.name.apply(get_last_name)

total_earned = lambda row: (row['hours_worked'] - 40) * row['hourly_wage'] * 1.5
										          + row['hourly_wage'] * 40 
							             if row['hours_worked'] > 40 else
								               row['hours_worked'] * row['hourly_wage']
df['total_earned'] = df.apply(total_earned, axis = 1) # axis is needed to specify row
```

## Aggregates

```python
mean	             # Average of all values in column
std	               # Standard deviation
median	           # Median
max	               # Maximum value in column
min	               # Minimum value in column
count	             # Number of values in column
nunique	           # Number of unique values in column
unique	           # List of unique values in column
np.percentile(<input>, <...<=reqd_percentile_value>...>)

df.groupby('column1').column2.measurement() # syntax
# .apply() .reset_index() and .rename() can be used as well in association

# example
high_earners = df.groupby('category').wage
    .apply(lambda x: np.percentile(x, 75))
    .reset_index()
df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()

# First use the groupby statement:
unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# Now pivot the table
pivoted = unpivoted.pivot(
    columns='Day of Week',
    index='Location',
    values='Total Sales')
```

## Multiple Tables

```python
big_df = orders.merge(customers).merge(products)
df = pd.merge(orders, customers)
df2 = pd.merge(
    orders,
    customers.rename(columns={'id': 'customer_id'}))

# Merges other than Inner Merge
pd.merge(company_a, company_b, how='outer') 
pd.merge(company_a, company_b, how='left')
pd.merge(company_a, company_b, how='right')

pd.concat([df1, df2, df2, ...])
```

<script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.6/MathJax.js?config=TeX-AMS_CHTML"></script>
