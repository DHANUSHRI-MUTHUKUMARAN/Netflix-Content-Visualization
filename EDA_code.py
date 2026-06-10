import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

# Set chart style
sns.set_theme(style='whitegrid', palette='muted')

print("Libraries loaded successfully!")

# Load dataset
df = pd.read_csv('netflix_titles.csv')

print(f"\nDataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Display first 3 rows
print("\n=== First 3 Rows ===")
print(df.head(3))

# Dataset information
print("\n=== Dataset Info ===")
df.info()

# Data types
print("\n=== Column Data Types ===")
print(df.dtypes)

# Missing values
print("\n=== Missing Values ===")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)

missing_df = pd.DataFrame({
    'Missing Count': missing,
    'Missing Percentage': missing_pct
})

print(missing_df[missing_df['Missing Count'] > 0])

# Summary statistics
print("\n=== Summary Statistics ===")
print(df.describe())

# Content type split
print("\n=== Content Type Split ===")
print(df['type'].value_counts())

# Top countries
print("\n=== Top 5 Countries ===")
print(df['country'].value_counts().head(5))

# Top ratings
print("\n=== Top 5 Ratings ===")
print(df['rating'].value_counts().head(5))

# Release year statistics
print("\n=== Release Year Statistics ===")
print(df['release_year'].describe())

# Visualization
yearly = df.groupby(['release_year', 'type']).size().unstack(fill_value=0)
yearly = yearly[yearly.index >= 2000]

fig, ax = plt.subplots(figsize=(12, 5))

yearly.plot(
    kind='bar',
    ax=ax,
    width=0.8
)

ax.set_title('Netflix Content by Release Year (2000+)', fontsize=14)
ax.set_xlabel('Release Year')
ax.set_ylabel('Number of Titles')
ax.legend(title='Type')

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

print("\nWeek 1 completed successfully!")