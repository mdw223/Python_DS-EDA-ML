Lectures 12-16

# Exploratory Data Analysis

Libraries: pandas, matplotlib, searbon, plotly

import matplotlib.pyplot as plt

data = [10, 22, 33...]
plt.plot(data)
can take 2 param like plt.plot(x, y)
can also plot a series
plt.plot(pd.Series([1,2,3], index=[2,3,5]))
series_a.plot() is another way

plt.title('...')
plt.xlabel('...')

.mean()
gb = df.groupby(['size',...])['percent'].mean()
gp.unstack().plot() # to get normal x axis

Multiple plots:
plt.plot(..., label = '...')
plt.plot(..., label = '...')
plt.legend() # or can pass a list in here

# Types of plots used for data visualization of continuous and categorical variables, recognizing plot created through given code 

// This method gets you normal line graphs 
plt.plot(data, marker = 'o') // for circle points graph 

fix, axes = plt.subplots() // plot different data on the same graph/axis
axes.plot(data1['x'], data1['y'], 'o', label='data1')
axes.plot(data2['x'], data2['y'], 'o', label='data2')

can also create subplots like
fig = plt.figure()
axes1 = fig.add_subplot(2, )


## Other types 

line g.plot.line(...)
scatter tips.plot.scatter(x = 'bill', y = 'tip')
bar  tips['size'].value_counts().plot(kind='bar')
histogram     plt.hist(tips['percent'], bins=100)
density      tips.plot.density(y='bill')
box         tips[['bill', 'percent']].plot.box()
pie     tips.groupby('size')['tip'].sum().plot.pie()

# Import Seaborn

import seaborn as sns
bar    sns.catplot(data=tips, kind='bar', x='smoker', y='percent')

# Plotly
Inveractive as you can hover over the graphs 

# EDA STEPS
Load data, destinguish attributes, univariate analysis, bivariate and multivariate, detect missing valyes, find outliers,...

# Causation vs. correlation, identifying and quantifying correlation 
Age of Miss America corrolates with Murders by hot things objects
Causation is when lack of ram causes phone to freeze.

In graphs, you can Use scatter plots and a line of best fit to show how correlated the data is. Beware of overplotting.
r-value is the correlation coefficient. -1 <= r <= 1 where 0 means no correlation

With 2 categorical varibales, or more, can use a heat map to show stregth of correlation.

Can use sns.pairplot(data=mpg, y_vars[...]. x_vars=[...], diag_kind='kde')
this shows many graphs with the different variables as the x and y 

can check how correlatied by doing .corr() on a dataset
you can then put that in a heatmap like 
sns.heatmap(data=mpg.corr())

# Simple and multiple regression, underfitting vs. overfitting, predictive analysis

For variables that appear to have some correlation, we want a predictive model. Linear regression model that finds the best fit linear relationship between a response (dependent) variable and a predictor (independent) variable. You can use many predictors.

Use statsmodels package.
import statsmodels.formula.api as smf

results = smf.ols(formula='tip ~ total_bill', data=tips).fit()
// here the tip is the y
// and the total bill is x (predictor/independent variable)

can graph a line of best fit on a scatter plot easy like
sns.regplot(x='total_bill', y='tip', ci=None, data=tips)

if you want access to the predicted values however, then you need to do
results.params using smf 
then do y=mx+b
tips['line']=tips['total_bill'] * results.params[1] + results.params[0]


## multiple regression

in the formala do
reults = smf.ols(formula= 'tip ~ total_bill + size', data=tips).fit()
tip = 0.0927 * total_bill + 0.1926 * size + 0.6689 
// those numbers are the coefficints
results.params gets you the coefficients you need 

You can then visualize this using a 3D meshgrid

For polynomial fitting for multiple veriables...:
sns.lmplot(data=mpg, x='disp', y='cty', ci=None,markets='d',order=2)
you can change the order to fit it more or less

to get the equation:
coefs = np.polyfit(mpg['displ'], mpg['cty'], 2) # degree of 2
polynomial = np.ploy1d(coefficients)

# Combining datasets through concatenation and merges

pd.concat([df1, df2], ignore_index=True) # resets the index
                        axis=1 is to concat a df into columns
                        axis=0 is default (will add rows)

pets.merge(breeders, left_on='petname', right_on='Dogname')
pets.merge(breeders, how='left')


# Data cleaning techniques, issues with untidy data, date formats 

Cleaning
Munging is changing data to another format
Wrangling is munging, data viz, agg, training...

Missing data can come from: empty cells, merged data, re-indexing, propagation thru calculations

to count missing vals:
 np.count_nonzero(life.isnull())

Replace the nan's
new = df.fillna(0) OR df.fillna(0, inplace=True)

.dropna() // drops those rows

.ffill() or .bfill() tries to give avg numbers


.drop_duplicates()

.rename(columns={'index': 'patient_id'})

df.T to transpose

## Aggregation with groupby()
.count(), .sum(), max(), mean(), ...

Long data - better for analysis
Wide data - human readable

Long is when instead of each rows's name of the person being unique, 
there are many rows with the same name but the columns like jan, feb get collapsed into a single month column...

data.drop(columns=['Name'], inplace=True)

make categorical:
df['col_str'] = df['col'].astype(str)

pd.to_datetime(date) # timestamp
str(date2)[:10] # get date. or date2.date