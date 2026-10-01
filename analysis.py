import pandas as pd

# Load dataset
df = pd.read_csv("healthcare_patients.csv")

# Explore dataset
print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# Identify column types
print("\nColumn Data Types:")
print(df.dtypes)

categorical_cols = df.select_dtypes(include="object").columns
numeric_cols = df.select_dtypes(include="number").columns

print("\nCategorical Columns:", list(categorical_cols))
print("Numerical Columns:", list(numeric_cols))

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing numerical values with median
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values with mode
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Basic analysis
print("\n--- BASIC ANALYSIS ---")

print("Total Patient Records:", len(df))

if "Patient_ID" in df.columns:
    print("Unique Patients:", df["Patient_ID"].nunique())

if "Age" in df.columns:
    print("Average Age:", round(df["Age"].mean(), 2))

if "Disease" in df.columns:
    print("\nMost Common Diseases:")
    print(df["Disease"].value_counts())

if "Gender" in df.columns:
    print("\nGender Distribution:")
    print(df["Gender"].value_counts())

# Save cleaned dataset
df.to_csv("cleaned_healthcare_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")