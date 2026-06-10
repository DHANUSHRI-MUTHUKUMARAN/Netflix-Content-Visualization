import pandas as pd
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')

print("Libraries loaded successfully!")

# Load dataset
df = pd.read_csv('netflix_titles.csv')

print(f"\nDataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Create a copy
df_clean = df.copy()

# ==========================
# Missing Values Before Cleaning
# ==========================
print("\n=== Missing Values Before Cleaning ===")
print(df_clean.isnull().sum())

# ==========================
# Fill Missing Values
# ==========================
df_clean['director'] = df_clean['director'].fillna('Unknown')
df_clean['cast'] = df_clean['cast'].fillna('Unknown')
df_clean['country'] = df_clean['country'].fillna('Unknown')

# Remove rows with missing critical values
df_clean.dropna(
    subset=['date_added', 'rating', 'duration'],
    inplace=True
)

# ==========================
# Clean and Convert Date Column
# ==========================
df_clean['date_added'] = df_clean['date_added'].str.strip()

df_clean['date_added'] = pd.to_datetime(
    df_clean['date_added'],
    errors='coerce'
)

# Remove invalid dates
df_clean.dropna(subset=['date_added'], inplace=True)

# Extract year and month added
df_clean['year_added'] = df_clean['date_added'].dt.year
df_clean['month_added'] = df_clean['date_added'].dt.month

# ==========================
# Clean Duration Column
# ==========================
df_clean['duration_num'] = (
    df_clean['duration']
    .str.extract(r'(\d+)')
    .astype(int)
)

# ==========================
# Missing Values After Cleaning
# ==========================
print("\n=== Missing Values After Cleaning ===")
print(df_clean.isnull().sum())

# ==========================
# Dataset Information
# ==========================
print("\n=== Clean Dataset Info ===")
df_clean.info()

# Dataset Shape
print("\n=== Clean Dataset Shape ===")
print(df_clean.shape)

# Preview
print("\n=== First 5 Rows ===")
print(df_clean.head())

# ==========================
# Save Cleaned Dataset
# ==========================
df_clean.to_csv(
    'netflix_titles_cleaned.csv',
    index=False
)

print("\n✅ Cleaned dataset saved as 'netflix_titles_cleaned.csv'")
print("✅ Week 2 Data Cleaning completed successfully!")