import pandas as pd
import numpy as np

#load raw caluclator
df_calendar=pd.read_csv("data/calendar.csv")
#simulate prices between $50 to $300
df_calendar["price"]=np.random.randint(50,300, size=len(df_calendar))

#clean 'available' column
df_calendar["available"]=df_calendar["available"].map({"t":True, "f":False})

#convert date coloumn
df_calendar["date"]=pd.to_datetime(df_calendar["date"],errors="coerce")
#drop any rows with bad dates or IDs
df_calendar.dropna(subset=["listing_id","date","price"],inplace=True)

#save simulated version
df_calendar.to_csv("outputs/simulated_calendar.csv", index=False)
print("Simulated Calender data saved. Rows :" , df_calendar.shape[0])
print ("Sample output :" , df_calendar.columns.tolist(0))