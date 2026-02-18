# Amazon Sentiment Analysis

This project performs sentiment analysis on Amazon product reviews using Python, Pandas, TextBlob, and Matplotlib.

## Description

The analysis loads Amazon review data from `amazon.csv`, cleans it by removing missing review texts, computes sentiment polarity scores using TextBlob, classifies sentiments into positive, negative, or neutral categories, and provides visualizations and statistics on how text sentiment aligns with numerical ratings.

## Requirements

- Python 3.x
- pandas
- textblob
- matplotlib

Install dependencies with:
```
pip install pandas textblob matplotlib
```

## Data

The dataset `amazon.csv` contains Amazon product reviews with columns:
- asin: Product ID
- reviewText: Review text
- overall: Rating (1-5)
- category: Category
- summary: Review summary

## Usage

1. Ensure `amazon.csv` is in the same directory.
2. Run the Jupyter notebook `sentimentanalysis.ipynb` or the Python script `sentiment_analysis.py`.
3. The notebook includes code to load data, perform analysis, and generate visualizations.

## Visualizations

- Bar chart of sentiment distribution
- Histogram of polarity scores
- Box plot of overall ratings by sentiment
- Pie chart of sentiment distribution

## Results

The analysis outputs average ratings by sentiment and various plots to visualize the data.
