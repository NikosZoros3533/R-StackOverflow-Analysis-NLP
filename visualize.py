import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import numpy as np
import datetime






# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('question_tag_R.csv')
# Convert the "creation_date" column to datetime format
df['creation_date'] = pd.to_datetime(df['creation_date'], unit='s')

# Compute the average score per day
daily_scores = df.groupby(pd.Grouper(key='creation_date', freq='D')).mean()['score']

# Create a line chart of the daily average scores
plt.plot(daily_scores.index, daily_scores.values)

# Set the plot title and axis labels
plt.title('Average Score for R Questions Over Time')
plt.xlabel('Date')
plt.ylabel('Average Score')
plt.xlim(pd.Timestamp('2008-01-01'), pd.Timestamp('2018-12-31'))

# Show the plot
plt.show()

















"""
Creation of R questions during time


# Set the plot style to "ggplot"
plt.style.use('ggplot')
# Read the CSV file into a Pandas DataFrame object
df = pd.read_csv("question_tag_R.csv")
# Convert the creation_date column to a datetime object
df['creation_date'] = df['creation_date'].apply(lambda x: datetime.datetime.utcfromtimestamp(x))
# Extract the year and month from the creation_date column
df['year_month'] = df['creation_date'].dt.to_period('M')
# Group the DataFrame by year_month and count the number of questions in each group
grouped = df.groupby('year_month')['question_id'].count()
# Create a line chart of the number of R questions over time
plt.plot(grouped.index.astype(str), grouped.values, '-o')
plt.xlabel('Year-Month')
plt.ylabel('Number of R Questions')
plt.title('Growth of R on Stack Overflow')
# Add a grid to the plot
plt.grid(axis='y')
# Rotate the x-axis labels
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))
# Adjust the figure size and save the figure
plt.gcf().set_size_inches(12, 6)
plt.savefig('r_growth.png', dpi=300, bbox_inches='tight')
plt.show()









Creation of barchart with the frequencies of tags



# Load the data from the CSV file
df = pd.read_csv('question_tag_R.csv')
tags = df['tags'].apply(lambda x: x.split(',')) # split tags by comma and create a list of lists
tag_list = [tag.strip("'[] ") for tags_ in tags for tag in tags_] # create a flattened list of tags
tag_counts = pd.Series(tag_list).value_counts().sort_values(ascending=False)[1:11] # count the top 10 tags excluding 'r'
plt.bar(tag_counts.index, tag_counts.values)
plt.title('Top 10 Most Frequent Tags')
plt.xlabel('Tags')
plt.ylabel('Count')
plt.show()






Pie chart


# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('question_tag_R.csv')

# Calculate the number of answered and unanswered questions
answered_count = df['is_answered'].sum()
unanswered_count = len(df) - answered_count

# Calculate the percentage of answered and unanswered questions
answered_percentage = answered_count / len(df) * 100
unanswered_percentage = 100 - answered_percentage

# Create a pie chart with two slices, one for answered and one for unanswered
fig, ax = plt.subplots()
ax.pie([answered_percentage, unanswered_percentage], labels=['Answered', 'Unanswered'], autopct='%1.1f%%')

# Set the title
ax.set_title('Answered vs Unanswered Questions')

# Show the plot
plt.show()






Create a scatter plot views answer
  
df = pd.read_csv('question_tag_R.csv')

plt.scatter(df['answer_count'], df['view_count'], s=10)

# Set the plot title and axis labels
plt.title('Relationship between View Count and Answer Count')
plt.xlabel('Answer Count')
plt.ylabel('View Count')

plt.ylim(min(df['view_count'])-1, max(df['view_count'])+1)



def format_fn(value, tick_number):
    return int(value)


plt.gca().yaxis.set_major_formatter(FuncFormatter(format_fn))
# Show the plot
plt.show()







Create the density plot kde


xlim = (0, 50000)

# Create a density plot of the view count distribution
sns.kdeplot(data=df, x='view_count', fill=True)
plt.xlim(xlim)


# Set the plot title and axis labels
plt.title('Distribution of View Count for R Questions')
plt.xlabel('View Count')
plt.ylabel('Density')
plt.show()









"""
