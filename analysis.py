import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for "Tower of God"
data = {
    'Page': ['Page 1', 'Page 2', 'Page 3', 'Page 4', 'Page 5'],
    'Page Views': [1200, 1500, 1100, 900, 1000],
    'Avg Time Spent (min)': [5.5, 6.2, 4.8, 3.9, 4.5],
    'Bounce Rate (%)': [35, 30, 40, 45, 38]
}

df = pd.DataFrame(data)

# Visualization of page views
plt.figure(figsize=(8, 5))
sns.barplot(x='Page', y='Page Views', data=df, palette='viridis')
plt.title('Page Views for Tower of God')
plt.xlabel('Page')
plt.ylabel('Views')
plt.show()

# Visualization of average time spent
plt.figure(figsize=(8, 5))
sns.lineplot(x='Page', y='Avg Time Spent (min)', data=df, marker='o')
plt.title('Average Time Spent per Page')
plt.xlabel('Page')
plt.ylabel('Avg Time Spent (min)')
plt.show()

# Visualization of bounce rate
plt.figure(figsize=(8, 5))
sns.barplot(x='Page', y='Bounce Rate (%)', data=df, palette='coolwarm')
plt.title('Bounce Rate per Page')
plt.xlabel('Page')
plt.ylabel('Bounce Rate (%)')
plt.show()
