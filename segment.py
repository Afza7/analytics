import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample user segmentation data
segment_data = {
    'Segment': ['Age 18-24', 'Age 25-34', 'Age 35-44', 'Returning Visitors', 'New Visitors'],
    'Avg Time Spent (min)': [4.8, 5.3, 4.0, 5.5, 3.9],
    'Page Views': [1800, 1500, 700, 2000, 800]
}

segment_df = pd.DataFrame(segment_data)

# Visualization of user segments
plt.figure(figsize=(10, 6))
sns.barplot(x='Segment', y='Avg Time Spent (min)', data=segment_df, palette='plasma')
plt.title('Average Time Spent by User Segment')
plt.xlabel('User Segment')
plt.ylabel('Avg Time Spent (min)')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Segment', y='Page Views', data=segment_df, palette='viridis')
plt.title('Page Views by User Segment')
plt.xlabel('User Segment')
plt.ylabel('Page Views')
plt.show()
