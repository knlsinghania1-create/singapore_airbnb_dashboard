import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("outputs/clean_listings.csv")

# Group by neighborhood group
region_counts = df["neighbourhood_group"].value_counts()

# Plot
region_counts.plot(kind="bar", color="teal")
plt.title("Number of Listings by Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/listings_by_region.png")
plt.show()
