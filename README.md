# 🌍 World Happiness Report Analysis (2015-2019)

A full data analysis project exploring global happiness trends across 170 countries
using the World Happiness Report dataset (2015-2019).

This project covers the complete data analysis life cycle from raw data cleaning
to exploratory analysis, visualization, and predictive modeling.


## 📁 Project Structure

    world-happiness-analysis/
    ├── data/
    │   ├── raw/                    # Original CSV files (2015-2019)
    │   └── processed/              # Cleaned and merged dataset
    ├── scripts/
    │   ├── 01_data_cleaning.py     # Data cleaning and merging
    │   ├── 02_eda.py               # Exploratory data analysis
    │   ├── 03_visualization.py     # Charts and visualizations
    │   └── 04_modeling.py          # Regression modeling
    ├── outputs/
    │   └── figures/                # All saved charts (PNG)
    ├── README.md
    └── requirements.txt

## 📊 Dataset

- **Source:** [Kaggle - World Happiness Report](https://www.kaggle.com/datasets/unsdsn/world-happiness)
- **Years covered:** 2015, 2016, 2017, 2018, 2019
- **Countries:** 170 unique countries
- **Records:** 782 rows after merging all years

## 🔧 Tools & Libraries

- Python 3
- pandas
- matplotlib
- seaborn
- scikit-learn

Install dependencies:

    pip install pandas matplotlib seaborn scikit-learn

## 🔄 How to Run

Run the scripts in order from the project root directory:

    py scripts/01_data_cleaning.py
    py scripts/02_eda.py
    py scripts/03_visualization.py
    py scripts/04_modeling.py

## 🔍 Key Findings

### Data Cleaning
- Standardized inconsistent column names across all 5 years
- Filled 1 missing value in the 2018 corruption column using median imputation
- Merged all years into a single clean dataset of 782 rows and 11 columns

### Exploratory Data Analysis
- **Happiest countries:** Denmark, Norway, Finland, Switzerland, Iceland
- **Least happy countries:** Burundi, Central African Republic, Syria
- **Global happiness** remained stable between 5.35 and 5.41 over 5 years
- **GDP per capita** has the strongest correlation with happiness (r = 0.789)
- **Generosity** has the weakest correlation (r = 0.138)
- **Australia/New Zealand** and **North America** are the happiest regions
- **Venezuela** had the sharpest happiness decline (−2.103) from 2015 to 2019
- **Benin** showed the greatest improvement (+1.543)

### Modeling
| Model | R² | RMSE | CV R² |
|-------|----|------|-------|
| Linear Regression | 0.7291 | 0.5740 | 0.7394 |
| Random Forest | 0.7885 | 0.5072 | 0.7787 |

- **Random Forest** outperformed Linear Regression on all metrics
- **GDP per capita** was the most important feature (importance = 0.519)
- **Life expectancy** ranked second (0.212)
- Both models were validated using 5-fold cross validation

## 📈 Visualizations

| # | Chart | Description |
|---|-------|-------------|
| 1 | Top & Bottom 10 Countries | Average happiness score 2015-2019 |
| 2 | Global Trend | Average happiness score per year |
| 3 | Correlation Heatmap | Relationships between all factors |
| 4 | GDP vs Happiness | Scatter plot of strongest predictor |
| 5 | Happiness by Region | Regional comparison (2015-2016) |
| 6 | Most Improved vs Declined | Country-level change 2015 to 2019 |
| 7 | Actual vs Predicted | Model performance comparison |
| 8 | Feature Importance | Random Forest feature ranking |
| 9 | Model Comparison | R² and RMSE side by side |


