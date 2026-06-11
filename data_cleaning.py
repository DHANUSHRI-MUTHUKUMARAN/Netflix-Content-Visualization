import pandas as pd
import numpy as np
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

print("Libraries loaded successfully!")

# Load dataset
df = pd.read_csv('netflix_titles.csv')

print(f"\nDataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ==================================================
# Missing Values Before Cleaning
# ==================================================

print("\n=== Missing Values Before Cleaning ===")
print(df.isnull().sum())

# Create copy
df_clean = df.copy()

# ==================================================
# Handle Missing Values
# ==================================================

df_clean['director'] = df_clean['director'].fillna('Unknown')
df_clean['cast'] = df_clean['cast'].fillna('Unknown')
df_clean['country'] = df_clean['country'].fillna('Unknown')

# Fill rating with mode
df_clean['rating'] = df_clean['rating'].fillna(
    df_clean['rating'].mode()[0]
)

# ==================================================
# Date Cleaning
# ==================================================

df_clean['date_added'] = pd.to_datetime(
    df_clean['date_added'].astype(str).str.strip(),
    errors='coerce'
)

# Extract Year and Month Added
df_clean['year_added'] = df_clean['date_added'].dt.year
df_clean['month_added'] = df_clean['date_added'].dt.month_name()

# ==================================================
# Duration Cleaning
# ==================================================

df_clean['duration_num'] = pd.to_numeric(
    df_clean['duration'].str.extract(r'(\d+)')[0],
    errors='coerce'
)

# Separate Movies and TV Shows
movie_dur = df_clean[df_clean['type'] == 'Movie']['duration_num']
show_seasons = df_clean[df_clean['type'] == 'TV Show']['duration_num']

# ==================================================
# Remove Duplicate Records
# ==================================================

before_rows = len(df_clean)

df_clean = df_clean.drop_duplicates()

after_rows = len(df_clean)

print(f"\nRows removed: {before_rows - after_rows}")

# ==================================================
# Missing Values After Cleaning
# ==================================================

print("\n=== Missing Values After Cleaning ===")

remaining_missing = df_clean.isnull().sum()
print(remaining_missing[remaining_missing > 0])

# ==================================================
# Save Cleaned Dataset
# ==================================================

df_clean.to_csv(
    'netflix_titles_cleaned.csv',
    index=False
)

# ==================================================
# Cleaning Summary
# ==================================================

print("\n=== Cleaning Summary ===")
print(f"Original Rows : {len(df)}")
print(f"Cleaned Rows  : {len(df_clean)}")
print(f"Columns       : {df_clean.shape[1]}")

print("\nDataset cleaned successfully!")
print("Saved as: netflix_titles_cleaned.csv")

# ==================================================
# Duration Statistics
# ==================================================

print("\n=== Duration Statistics ===")

if not movie_dur.empty:
    print(f"Average Movie Duration : {movie_dur.mean():.2f} minutes")

if not show_seasons.empty:
    print(f"Average TV Show Length : {show_seasons.mean():.2f} seasons")