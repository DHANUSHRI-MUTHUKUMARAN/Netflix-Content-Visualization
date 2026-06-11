# Netflix Content Visualization

Exploratory data analysis and visualization of Netflix's global content catalog using Python.

## Files

| File                         | Purpose                                                                  |
| ---------------------------- | ------------------------------------------------------------------------ |
| `data_cleaning.py`           | Cleans raw data, handles missing values, parses dates, extracts duration |
| `EDA_code.py`                | Initial exploratory data analysis and summary statistics                 |
| `visualization.py`           | Generates visualizations and saves charts                                |
| `netflix_titles.csv`         | Raw dataset                                                              |
| `netflix_titles_cleaned.csv` | Cleaned dataset                                                          |

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## How to Run

```bash
pip install pandas numpy matplotlib seaborn
python data_cleaning.py
python EDA_code.py
python visualization.py
```

## Dataset

Netflix Movies and TV Shows Dataset from Kaggle:
https://www.kaggle.com/datasets/shivamb/netflix-shows

## Key Insights

* Movies account for approximately 70% of Netflix content.
* The United States is the largest content producer.
* India is the second-largest contributor.
* TV-MA is the most common rating.
* Netflix content additions peaked between 2018 and 2019.
