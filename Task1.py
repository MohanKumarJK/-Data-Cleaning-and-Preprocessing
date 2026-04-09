import pandas as pd

# 1. Load the dataset
# Replace 'your_data.csv' with your actual filename
df = pd.read_csv('netflix_cleaned.csv')

print("--- Initial Data Info ---")
print(df.info())

# 2. Rename column headers (Clean and uniform: lowercase, no spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 3. Identify and handle missing values
# Option A: Check count of nulls
print("\nMissing values per column:\n", df.isnull().sum())
# Option B: Fill missing values (example: fill numeric with mean, categorical with 'Unknown')
# df['age'] = df['age'].fillna(df['age'].mean())
# df['gender'] = df['gender'].fillna('Unknown')
# Or simply drop rows with any nulls:
df = df.dropna()

# 4. Remove duplicate rows
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates()
print(f"\nRemoved {duplicate_count} duplicate rows.")

# 5. Standardize text values (Example: Gender or Country)
# Ensures 'Male', 'male', ' M ' all become 'male'
if 'gender' in df.columns:
    df['gender'] = df['gender'].str.strip().str.lower()

# 6. Check and fix data types (e.g., age to int)
# Using errors='coerce' turns non-numeric junk into NaN, which we then drop
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce').astype(int)

# 7. Convert date formats to a consistent type (dd-mm-yyyy)
# First convert to datetime objects, then format as string if needed
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    # If the deliverable requires a specific string format:
    # df['date'] = df['date'].dt.strftime('%d-%m-%Y')

# 8. Save the cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)

print("\n--- Cleaning Complete ---")
print(f"Final shape: {df.shape}")