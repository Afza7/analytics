import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated A/B test results
ab_test_data = {
    'Group': ['A', 'B'],
    'Headline': ['Old Headline', 'New Engaging Headline'],
    'Avg Time Spent (min)': [3.2, 4.5],
    'Bounce Rate (%)': [42, 30]
}

ab_df = pd.DataFrame(ab_test_data)

# Comparison of A/B test results
plt.figure(figsize=(8, 5))
sns.barplot(x='Group', y='Avg Time Spent (min)', data=ab_df, palette='magma')
plt.title('A/B Test - Average Time Spent')
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x='Group', y='Bounce Rate (%)', data=ab_df, palette='coolwarm')
plt.title('A/B Test - Bounce Rate')
plt.show()
