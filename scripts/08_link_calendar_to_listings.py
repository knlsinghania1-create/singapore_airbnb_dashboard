import pandas as pd

#Load listings and simulated calender

df_listings=pd.read_csv("outputs/clean_listings.csv")
df_calender=pd.read_csv("outputs/simulated_calendar.csv")

#convert types

df_calender["listing_id"]=pd.to_numeric(df_calender["listing_id"],errors="coerce")
df_listings["id"]=pd.to_numeric(df_listings["id"], errors="coerce")

# Merge on ID
df_combined= pd.merge(df_calender,df_listings,left_on="listing_id",right_on="id",how="inner")

# Save merged output

df_combined.to_csv("outputs/calender_with_listing_data.csv", index=False)

#status

print("Merged Calendar with listing data")
print("Total rows : " , df_combined.shape[0])