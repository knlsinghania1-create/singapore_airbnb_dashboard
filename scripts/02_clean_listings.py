import pandas as pd

# Load merged listings
df = pd.read_csv("outputs/merged_listing.csv")

# 🔧 Clean price column
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# 🎯 Select key columns for analysis
columns_to_keep = [
    "id", "name", "neighbourhood_group", "neighbourhood",
    "latitude", "longitude", "room_type", "price",
    "minimum_nights", "number_of_reviews",
    "reviews_per_month", "availability_365"
]

df_clean = df[columns_to_keep].dropna()

# 💾 Save cleaned version
df_clean.to_csv("outputs/clean_listings.csv", index=False)

# ✅ Print basic stats
print("Cleaned listings saved successfully.")
print("Total rows:", df_clean.shape[0])
print("Sample neighborhoods:", df_clean['neighbourhood'].unique()[:5])
