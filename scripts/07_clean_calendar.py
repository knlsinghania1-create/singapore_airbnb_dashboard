import pandas as pd
#load calendar data
df_calendar=pd.read_csv("data/calendar.csv")
#clean price volume
df_calendar["price"]=(df_calendar["price"].replace(['\$'],'',regex=True).astype(float))

#convert date into datetime

df_calendar["date"]=pd.to_datetime(df_calendar["date"], errors="coerce")
#Drop nulls & reset index
df_calendar.dropna(subset=["listing_id","date","price"], inplace=True)
df_calendar.reset_index(drop=True, inplace=True)

#save clean version
df_calendar.to_csv("outputs/clean_calendar.csv", index=False)
print("Calendar cleaned and saved")
print("Total Rows : ", df_calendar.shape[5])
