import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os

warnings.filterwarnings('ignore')
sns.set_theme(style='whitegrid')

print("Libraries loaded successfully!")

# Create output folder
os.makedirs("aggregation_images", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv('netflix_titles_cleaned.csv')

print(f"\nDataset loaded: {df.shape}")

# =====================================================
# 1. Top 15 Countries
# =====================================================

top_countries = df['country'].value_counts().head(15)

print("\n=== Top 15 Countries ===")
print(top_countries)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title('Top 15 Countries by Netflix Content')
plt.xlabel('Number of Titles')
plt.ylabel('Country')

plt.tight_layout()
plt.savefig(
    'aggregation_images/top15_countries.png',
    dpi=150,
    bbox_inches='tight'
)
plt.show()

# =====================================================
# 2. Top 15 Directors
# =====================================================

top_directors = (
    df[df['director'] != 'Unknown']['director']
    .value_counts()
    .head(15)
)

print("\n=== Top 15 Directors ===")
print(top_directors)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_directors.values,
    y=top_directors.index
)

plt.title('Top 15 Directors on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Director')

plt.tight_layout()
plt.savefig(
    'aggregation_images/top15_directors.png',
    dpi=150,
    bbox_inches='tight'
)
plt.show()

# =====================================================
# 3. Movies vs TV Shows by Country
# =====================================================

country_type = pd.crosstab(
    df['country'],
    df['type']
)

top_country_type = country_type.sum(axis=1)\
                               .sort_values(ascending=False)\
                               .head(10)

country_type = country_type.loc[top_country_type.index]

print("\n=== Movies vs TV Shows by Top Countries ===")
print(country_type)

country_type.plot(
    kind='bar',
    figsize=(12, 6)
)

plt.title('Movies vs TV Shows by Country')
plt.xlabel('Country')
plt.ylabel('Number of Titles')

plt.tight_layout()
plt.savefig(
    'aggregation_images/country_type_comparison.png',
    dpi=150,
    bbox_inches='tight'
)
plt.show()

# =====================================================
# 4. Top 20 Genres
# =====================================================

genres = (
    df['listed_in']
    .str.split(', ')
    .explode()
)

top_genres = genres.value_counts().head(20)

print("\n=== Top 20 Genres ===")
print(top_genres)

plt.figure(figsize=(10, 7))
sns.barplot(
    x=top_genres.values,
    y=top_genres.index
)

plt.title('Top 20 Netflix Genres')
plt.xlabel('Count')
plt.ylabel('Genre')

plt.tight_layout()
plt.savefig(
    'aggregation_images/top20_genres.png',
    dpi=150,
    bbox_inches='tight'
)
plt.show()

# =====================================================
# 5. Content Added Per Year
# =====================================================

yearly_content = (
    df.groupby('year_added')
    .size()
    .sort_index()
)

print("\n=== Content Added Per Year ===")
print(yearly_content)

plt.figure(figsize=(12, 5))
sns.lineplot(
    x=yearly_content.index,
    y=yearly_content.values,
    marker='o'
)

plt.title('Netflix Content Added Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')

plt.tight_layout()
plt.savefig(
    'aggregation_images/content_added_per_year.png',
    dpi=150,
    bbox_inches='tight'
)
plt.show()

# =====================================================
# 6. Average Movie Duration
# =====================================================

movie_duration = (
    df[df['type'] == 'Movie']
    ['duration_num']
)

print("\n=== Movie Duration Statistics ===")
print(movie_duration.describe())

# =====================================================
# 7. Average TV Show Seasons
# =====================================================

tv_seasons = (
    df[df['type'] == 'TV Show']
    ['duration_num']
)

print("\n=== TV Show Season Statistics ===")
print(tv_seasons.describe())

print("\n===================================")
print("AGGREGATION & GROUPING COMPLETE")
print("===================================")

print(f"\nAverage Movie Duration : {movie_duration.mean():.1f} mins")
print(f"Average TV Show Seasons: {tv_seasons.mean():.1f}")

print("\nCharts saved inside:")
print("aggregation_images/")