
import pandas as pd
import matplotlib.pyplot as plt
# 1 - Read dataset
# load the database
fraud_dataset = pd.read_csv("fraud_detection Dataset.csv")

# analyzing database and print some information about database
First_5_rows = fraud_dataset.head() # print first 5 rows of database
#print(First_5_rows)
# print database information
database_information = fraud_dataset.info()
#print(database_information)
# print database description
database_description = fraud_dataset.describe()
#print(database_description)

# 2 - Explore the data
# 1 - basic Exploration
print("First few rows of the dataset:")
print(fraud_dataset.head(10))

# Drop irrelevant columns (example: IDs)
irrelevant_columns = ['ID']  # put irrelevant columns to be dropped
for column in irrelevant_columns:
    if column in fraud_dataset.columns:
        fraud_dataset = fraud_dataset.drop(columns=irrelevant_columns)

# 2- Check Datatypes
print("\nColumn Datatypes:")
print(fraud_dataset.dtypes)  # Print the data types of each column

# Identify numerical and categorical columns
numerical_columns = fraud_dataset.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_columns = fraud_dataset.select_dtypes(include=['object']).columns.tolist()

print("\nNumerical Columns:", numerical_columns)
print("Categorical Columns:", categorical_columns)

# Convert categorical columns to 'category' datatype for better memory efficiency
for col in categorical_columns:
    fraud_dataset[col] = fraud_dataset[col].astype('category')
print("Print the data types of each column after Convert categorical columns to 'category' datatype")
print(fraud_dataset.dtypes)

# 3. Categorical Column Analysis
print("\nNumber of unique categories in each categorical column:")
for col in categorical_columns:
    print(f"{col}: {fraud_dataset[col].nunique()} unique categories")

# 4. Missing Values
print("\nMissing Values Analysis:")
missing_values = fraud_dataset.isnull().sum()  # Count of missing values in each column
missing_percentage = (missing_values / len(fraud_dataset)) * 100  # Percentage of missing values
print(missing_percentage)

# 3- handle missing values (our database doen't have missing values)
# 1. High Null Ratios: Drop columns with null-value percentage > 50%
high_null_cols = missing_percentage[missing_percentage > 50].index
print(f"Columns dropped due to high null ratio (>50%): {list(high_null_cols)}")
fraud_dataset = fraud_dataset.drop(columns=high_null_cols)

# 2. Categorical Columns: Fill missing values with the mode
for col in categorical_columns:
    mode_value = fraud_dataset[col].mode()  # Calculate the mode
    fraud_dataset[col].fillna(mode_value)


# 3. Numerical Columns: Visualize distribution and fill missing values
for col in numerical_columns:
    print(f"\nAnalyzing column: {col}")

    # Visualize the distribution
    plt.figure(figsize=(6, 4))
    fraud_dataset[col].hist(bins=30)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

    # Determine skewness
    skewness = fraud_dataset[col].skew()
    print(f"Skewness of {col}: {skewness}")

    if skewness > 0.5 or skewness < -0.5:  # Highly skewed
        median_value = fraud_dataset[col].median()
        print(f"Filling missing values in {col} with median: {median_value}")
        fraud_dataset[col].fillna(median_value)
    else:  # Symmetric distribution
        mean_value = fraud_dataset[col].mean()
        print(f"Filling missing values in {col} with mean: {mean_value}")
        fraud_dataset[col].fillna(mean_value)


