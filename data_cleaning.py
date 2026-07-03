import pandas as pd

# Load Netflix dataset (CSV file)
df = pd.read_csv("netflix_titles.csv")

# Display basic information
print("Dataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values in text columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna("Unknown")

# Convert date_added column to datetime
if "date_added" in df.columns:
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned file saved as: cleaned_dataset.csv")