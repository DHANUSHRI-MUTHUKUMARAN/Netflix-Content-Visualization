import streamlit as st
import pandas as pd

# ======================================
# Page Config
# ======================================

st.set_page_config(
    page_title="Netflix Content Dashboard",
    page_icon="🎬",
    layout="wide"
)

# ======================================
# Load Data
# ======================================

@st.cache_data
def load_data():
    return pd.read_csv("netflix_titles_cleaned.csv")

df = load_data()

# ======================================
# Header
# ======================================

st.title("🎬 Netflix Content Dashboard")
st.markdown("Interactive Analysis of Netflix Movies and TV Shows")

# ======================================
# Sidebar Filters
# ======================================

st.sidebar.header("Filters")

countries = sorted(df["country"].unique())

selected_country = st.sidebar.selectbox(
    "Country",
    ["All Countries"] + countries
)

selected_type = st.sidebar.selectbox(
    "Content Type",
    ["All", "Movie", "TV Show"]
)

ratings = sorted(df["rating"].unique())

selected_rating = st.sidebar.selectbox(
    "Rating",
    ["All"] + ratings
)

search_title = st.sidebar.text_input(
    "Search Title"
)

# ======================================
# Apply Filters
# ======================================

filtered_df = df.copy()

if selected_country != "All Countries":
    filtered_df = filtered_df[
        filtered_df["country"] == selected_country
    ]

if selected_type != "All":
    filtered_df = filtered_df[
        filtered_df["type"] == selected_type
    ]

if selected_rating != "All":
    filtered_df = filtered_df[
        filtered_df["rating"] == selected_rating
    ]

if search_title:
    filtered_df = filtered_df[
        filtered_df["title"]
        .str.contains(search_title, case=False, na=False)
    ]

# ======================================
# KPI Cards
# ======================================

total_titles = len(filtered_df)
movies = len(filtered_df[filtered_df["type"] == "Movie"])
tvshows = len(filtered_df[filtered_df["type"] == "TV Show"])
countries_count = filtered_df["country"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", total_titles)
col2.metric("Movies", movies)
col3.metric("TV Shows", tvshows)
col4.metric("Countries", countries_count)

st.divider()

# ======================================
# Dataset Preview
# ======================================

st.subheader("Dataset Preview")

st.dataframe(
    filtered_df[
        [
            "title",
            "type",
            "country",
            "release_year",
            "rating"
        ]
    ],
    use_container_width=True
)

# ======================================
# Content Type Distribution
# ======================================

st.subheader("Movies vs TV Shows")

type_counts = filtered_df["type"].value_counts()

st.bar_chart(type_counts)

# ======================================
# Ratings Distribution
# ======================================

st.subheader("Ratings Distribution")

rating_counts = filtered_df["rating"].value_counts()

st.bar_chart(rating_counts)

# ======================================
# Content Growth by Year
# ======================================

st.subheader("Content Added by Year")

year_counts = (
    filtered_df["year_added"]
    .value_counts()
    .sort_index()
)

st.line_chart(year_counts)

# ======================================
# Top Genres
# ======================================

st.subheader("Top Genres")

genres = (
    filtered_df["listed_in"]
    .str.split(", ")
    .explode()
)

genre_counts = genres.value_counts().head(10)

st.bar_chart(genre_counts)

# ======================================
# Top Countries
# ======================================

st.subheader("Top 10 Countries")

country_counts = (
    filtered_df["country"]
    .value_counts()
    .head(10)
)

st.bar_chart(country_counts)

# ======================================
# Duration Statistics
# ======================================

st.subheader("Duration Statistics")

if selected_type == "Movie":
    st.metric(
        "Average Movie Duration",
        f"{filtered_df['duration_num'].mean():.1f} mins"
    )

elif selected_type == "TV Show":
    st.metric(
        "Average TV Show Seasons",
        f"{filtered_df['duration_num'].mean():.1f}"
    )

# ======================================
# Footer
# ======================================

st.success("Dashboard Loaded Successfully!")
st.caption(
    "Netflix Content Visualization Project | Dhanushri Muthukumaran"
)