import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

# Ignore warnings
warnings.filterwarnings('ignore')

# Set chart style
sns.set_theme(style='whitegrid')

print("Libraries loaded successfully!")

# Create images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv('netflix_titles_cleaned.csv')

print(f"\nDataset loaded: {df.shape}")

# =====================================================
# 1. Movies vs TV Shows
# =====================================================
plt.figure(figsize=(6, 6))

df['type'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title('Movies vs TV Shows')
plt.ylabel('')

plt.savefig('images/movies_vs_tvshows.png')
plt.show()

# =====================================================
# 2. Top 10 Countries
# =====================================================
plt.figure(figsize=(10, 5))

top_countries = df['country'].value_counts().head(10)

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title('Top 10 Countries by Content')
plt.xlabel('Number of Titles')
plt.ylabel('Country')

plt.tight_layout()
plt.savefig('images/top_countries.png')
plt.show()

# =====================================================
# 3. Top Ratings
# =====================================================
plt.figure(figsize=(10, 5))

top_ratings = df['rating'].value_counts().head(10)

sns.barplot(
    x=top_ratings.index,
    y=top_ratings.values
)

plt.title('Top Ratings on Netflix')
plt.xlabel('Rating')
plt.ylabel('Count')

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('images/ratings.png')
plt.show()

# =====================================================
# 4. Content Added by Year
# =====================================================
plt.figure(figsize=(12, 5))

year_counts = (
    df['year_added']
    .value_counts()
    .sort_index()
)

sns.lineplot(
    x=year_counts.index,
    y=year_counts.values,
    marker='o'
)

plt.title('Netflix Content Added by Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')

plt.tight_layout()
plt.savefig('images/yearly_growth.png')
plt.show()

# =====================================================
# 5. Content Added by Month
# =====================================================
plt.figure(figsize=(10, 5))

month_counts = (
    df['month_added']
    .value_counts()
    .sort_index()
)

sns.barplot(
    x=month_counts.index,
    y=month_counts.values
)

plt.title('Content Added by Month')
plt.xlabel('Month')
plt.ylabel('Titles Added')

plt.tight_layout()
plt.savefig('images/monthly_additions.png')
plt.show()

# =====================================================
# 6. Movie Duration Distribution
# =====================================================
movies = df[df['type'] == 'Movie']

plt.figure(figsize=(10, 5))

sns.histplot(
    movies['duration_num'],
    bins=30,
    kde=True
)

plt.title('Movie Duration Distribution')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig('images/duration_distribution.png')
plt.show()

# =====================================================
# 7. Top 10 Genres
# =====================================================
genres = (
    df['listed_in']
    .str.split(', ')
    .explode()
)

top_genres = genres.value_counts().head(10)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)

plt.title('Top 10 Netflix Genres')
plt.xlabel('Count')
plt.ylabel('Genre')

plt.tight_layout()
plt.savefig('images/top_genres.png')
plt.show()

print("\n✅ All charts generated successfully!")
print("✅ Images saved in the 'images' folder.")
print("✅ Week 3 completed successfully!")