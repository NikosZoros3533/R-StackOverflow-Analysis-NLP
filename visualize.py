import pandas as pd
import matplotlib.pyplot as plt
import datetime


























"""


#  Set the plot style to "ggplot"
plt.style.use('ggplot')

# Read the CSV file into a Pandas DataFrame object
df = pd.read_csv("questionstagRwithoutdupls4.csv")

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













# Read the CSV file into a Pandas DataFrame object
df = pd.read_csv("questionstagRwithoutdupls4.csv")

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
plt.xticks(rotation=45)
plt.show()


"""
