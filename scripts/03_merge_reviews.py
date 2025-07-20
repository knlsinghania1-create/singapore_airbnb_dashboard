import pandas as pd
#load both review files
reviews1= pd.read_csv("data/reviews.csv")
reviews2=pd.read_csv("data/reviews2.csv")

#combine them
df_reviews=pd.concat([reviews1,reviews2],ignore_index=True)
#Save merged Review
df_reviews.to_csv("outputs/merged_reviews.csv", index=False)
#Show Progress
print("Merged reviews saved, Total rows :" , df_reviews.shape[0])
print("Sample Coloumn: ", df_reviews.columns.tolist())
