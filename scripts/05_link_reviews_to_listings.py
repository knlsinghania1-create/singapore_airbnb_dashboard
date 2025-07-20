import pandas as pd
#Load clean listing and reviews
df_listings= pd.read_csv("outputs/clean_listings.csv")
df_reviews=pd.read_csv("outputs/merged_reviews.csv")

#convert Date coloumn
df_reviews["listing_id"] = pd.to_numeric(df_reviews["listing_id"], errors="coerce")
df_listings["id"] = pd.to_numeric(df_listings["id"], errors="coerce")
df_reviews["date"]=pd.to_datetime(df_reviews["date"],errors="coerce")

# Merge on listing ID

df_combined=pd.merge(df_reviews,df_listings,left_on="listing_id",right_on="id",how="inner")

#save merged output
df_combined.to_csv("outputs/reviews_with_listing_data.csv", index=False)
#status
print("Reviews Successfully linked to listings")
print("Total rows in combined set : " , df_combined.shape[0])
print("Sample Columns :" , df_combined.columns.tolist())
