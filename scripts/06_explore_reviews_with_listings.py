import pandas as pd
import matplotlib.pyplot as plt

# Load combined review+listing dataset
df = pd.read_csv("outputs/reviews_with_listing_data.csv")

# 📍 Top-reviewed neighborhoods
top_neigh = df.groupby("neighbourhood")["comments"].count().sort_values(ascending=False)

top_neigh.plot(kind="bar", figsize=(10, 6), color="skyblue")
plt.title("Top Reviewed Neighborhoods in Singapore")
plt.xlabel("Neighborhood")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/top_reviewed_neighborhoods.png")
plt.show()

# 📊 Review volume vs. availability
df["month"] = pd.to_datetime(df["date"], errors="coerce").dt.to_period("M")
monthly_trend = df.groupby(["month", "room_type"]).size().unstack().fillna(0)

monthly_trend.plot(kind="line", marker="o", figsize=(10, 6))
plt.title("Monthly Review Trends by Room Type")
plt.xlabel("Month")
plt.ylabel("Review Count")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/monthly_roomtype_reviews.png")
plt.show()
