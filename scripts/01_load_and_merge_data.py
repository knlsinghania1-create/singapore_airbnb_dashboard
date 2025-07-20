import pandas as pd
listing1=pd.read_csv("data/listings.csv")
listing2=pd.read_csv("data/listings2.csv")

df_listings=pd.concat([listing1, listing2], ignore_index=True)
print("Listing is combined Successfully")
print("Total rows:", df_listings.shape[0])
print("Available Coloumn:" , df_listings.columns.tolist())
df_listings.to_csv("outputs/merged_listing.csv",index=False)
