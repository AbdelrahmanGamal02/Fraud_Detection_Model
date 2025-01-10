# Fraud_Detection_Model
## Overview
- This project is a Python-based fraud detection data analysis script. It processes a dataset to perform data exploration, cleaning, and initial statistical analysis. The primary goal is to prepare the data for further analysis or machine learning tasks by exploring its structure, handling missing values, and analyzing key features.

## Features
- The script provides the following functionalities:

### Data Loading and Exploration:

- Reads a CSV dataset file.
- Displays the first few rows of the dataset.
- Provides information about the data structure, types, and basic statistics.
### Data Cleaning:

- Removes irrelevant columns (e.g., ID).
- Converts categorical columns to a more memory-efficient category datatype.
### Handles missing values:
- Drops columns with more than 50% null values.
- Fills missing categorical values with the mode.
- Fills missing numerical values based on distribution (median for skewed data, mean for symmetric data).
### Data Analysis:

- Identifies numerical and categorical columns.
- Analyzes unique categories in categorical columns.
- Visualizes the distribution of numerical columns using histograms.
- Analyzes skewness of numerical data to decide on filling strategies.
### Dependencies
- Ensure the following Python libraries are installed:

- pandas
- matplotlib
  
### Usage
- Place the script (Fraud_Detection.py) and the dataset file (fraud_detection Dataset.csv) in the same directory.
- Run the script:  python Fraud_Detection.py
- The script will display the results of each processing step in the terminal and plot histograms for numerical data.
### Dataset
- The script expects the dataset to be in CSV format with the following assumptions:
  
- Both numerical and categorical data are included.
- Missing values may be present and will be handled based on pre-defined rules.
  
### Outputs
- The script provides:

- Summarized data structure and statistics.
- Cleaned dataset with missing values addressed.
- Visualizations of numerical data distributions.
### Customization
- To modify the script for specific use cases:

- Update the irrelevant_columns list to include additional columns for removal.
- Customize the threshold for dropping columns with high null values (50% by default).
- Modify the handling logic for missing values if different strategies are needed.

### AI model
- Split dataset into two sections :
- 80% of dataset is used for training phase
- 20% of dataset is used for test phase
  




