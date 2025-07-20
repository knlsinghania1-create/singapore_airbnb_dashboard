import pandas as pd
import matplotlib.pyplot as plt

#load merged reviews 
df_reviews=pd.read_csv("outputs/merged_reviews.csv")
#Basic Cleanup
df_reviews.dropna(subset=["listing_id","date","comments"],inplace=True)
#convert date into datetime
df_reviews["date"]=pd.to_datetime(df_reviews["date"],errors="coerce")
#review count by month
review_trend=df_reviews.groupby(df_reviews["date"].dt.to_period("M")).size()
#Plot review Trend

review_trend.plot(kind="line", color="Orange",marker="o")
plt.title("Monthly Review Volumens (Singapore)")
plt.xlabel("Month")
plt.ylabel("No. of Reviews")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/monthly_review_trend.png")
plt.show()
