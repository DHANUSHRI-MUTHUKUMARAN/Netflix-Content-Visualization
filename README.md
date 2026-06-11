# Netflix Content Visualization

## Project Overview

This project performs data cleaning, exploratory data analysis (EDA), and visualization on the Netflix Movies and TV Shows dataset. The goal is to uncover trends in Netflix's content library, including content growth, ratings distribution, genres, countries, and movie durations.

The project is built using Python and popular data analysis libraries such as Pandas, Matplotlib, and Seaborn.

---

## Dataset

**Dataset:** Netflix Movies and TV Shows

The dataset contains information about over 8,800 Netflix titles, including:

* Type (Movie / TV Show)
* Title
* Director
* Cast
* Country
* Date Added
* Release Year
* Rating
* Duration
* Genre
* Description

---

## Project Structure

| File                         | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| `netflix_titles.csv`         | Original Netflix dataset                                     |
| `data_cleaning.py`           | Data preprocessing and cleaning                              |
| `netflix_titles_cleaned.csv` | Cleaned dataset generated after preprocessing                |
| `EDA_code.py`                | Exploratory Data Analysis                                    |
| `visualization.py`           | Generates visualizations and saves them in the images folder |
| `images/`                    | Stores all generated charts                                  |
| `README.md`                  | Project documentation                                        |

---

## Data Cleaning Tasks

The following preprocessing steps were performed:

* Handled missing values in:

  * Director
  * Cast
  * Country
  * Rating
* Converted `date_added` to datetime format
* Extracted:

  * `year_added`
  * `month_added`
* Extracted numeric values from duration
* Created separate duration statistics for:

  * Movies (minutes)
  * TV Shows (seasons)
* Removed duplicate records
* Exported cleaned dataset for analysis

---

## Exploratory Data Analysis (EDA)

The EDA phase includes:

* Dataset shape and structure
* Data types inspection
* Missing value analysis
* Duplicate record analysis
* Summary statistics
* Content type distribution
* Top countries by content count
* Most common content ratings
* Release year analysis

---

## Visualizations Generated

The project generates the following visualizations:

1. Movies vs TV Shows Distribution
2. Top Countries by Number of Titles
3. Ratings Distribution
4. Content Added by Year
5. Monthly Content Additions
6. Movie Duration Distribution
7. Top Genres on Netflix

All charts are automatically saved in the `images/` folder.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## How to Run

### Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Run Data Cleaning

```bash
python3 data_cleaning.py
```

### Run Exploratory Data Analysis

```bash
python3 EDA_code.py
```

### Generate Visualizations

```bash
python3 visualization.py
```

---

## Sample Insights

* Movies make up the majority of Netflix content.
* The United States contributes the highest number of titles.
* Content additions increased significantly after 2015.
* Drama and International Movies are among the most popular genres.
* Most movies have a duration close to 100 minutes.

---

## Author

**Dhanushri Muthukumaran**

B.Tech Artificial Intelligence and Data Science

St. Joseph's College of Engineering

---

## License

This project is created for educational and learning purposes.
