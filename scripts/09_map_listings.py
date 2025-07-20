import pandas as pd
import folium

df = pd.read_csv("outputs/clean_listings.csv")
m = folium.Map(location=[1.3521, 103.8198], zoom_start=12)

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=3,
        color="blue",
        popup=f"{row['name']} (${row['price']})"
    ).add_to(m)

m.save("outputs/listings_basic_map.html")
