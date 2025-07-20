import streamlit as st
import pandas as pd

# 📥 Load Data
try:
    listings = pd.read_csv("outputs/clean_listings.csv")
    calendar = pd.read_csv("outputs/calendar_with_listing_data.csv")
    reviews = pd.read_csv("outputs/reviews_with_listing_data.csv")
    st.success("✅ Data loaded successfully")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# 🏠 Sidebar Navigation
st.sidebar.title("Singapore Airbnb Dashboard")
section = st.sidebar.radio("Choose a section:", [
    "Overview",
    "Listings Map",
    "Calendar Trends",
    "Review Insights"
])

# 📊 Section 1: Overview
if section == "Overview":
    st.title("📊 Singapore Airbnb Overview")
    st.write("Key metrics across listings, bookings, and reviews.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Listings", f"{listings.shape[0]:,}")
    col2.metric("Reviews", f"{reviews.shape[0]:,}")
    col3.metric("Calendar Entries", f"{calendar.shape[0]:,}")

# 🗺️ Section 2: Listings Map
elif section == "Listings Map":
    st.title("🗺️ Listings Map")
    st.write("Explore where Airbnb listings are located across Singapore.")

    try:
        map_html = open("outputs/listings_basic_map.html", "r").read()
        st.components.v1.html(map_html, height=600)
    except FileNotFoundError:
        st.warning("⚠️ Map file not found. Please generate `listings_basic_map.html` and place it in `outputs/`.")

# 📅 Section 3: Calendar Trends
elif section == "Calendar Trends":
    st.title("📅 Price Trends Over Time")
    st.write("Average daily price trends by neighborhood and month (June 2024 – June 2025).")

    try:
        calendar["date"] = pd.to_datetime(calendar["date"], errors="coerce")
        calendar["adjusted_price"] = pd.to_numeric(calendar["adjusted_price"], errors="coerce")
        calendar = calendar.dropna(subset=["date", "adjusted_price", "neighbourhood"])

        # Filter to target date range
        calendar = calendar[
            (calendar["date"] >= pd.to_datetime("2024-06-01")) &
            (calendar["date"] <= pd.to_datetime("2025-06-30"))
        ]

        calendar["year_month"] = calendar["date"].dt.to_period("M").astype(str)

        # 🎛️ Dropdowns with "All" options
        areas = sorted(calendar["neighbourhood"].unique())
        areas.insert(0, "All")

        months = sorted(calendar["year_month"].unique())
        months.insert(0, "All")

        selected_area = st.selectbox("Choose Neighborhood", areas)
        selected_month = st.selectbox("Choose Month (YYYY-MM)", months)

        # Filter logic
        filtered = calendar.copy()
        if selected_area != "All":
            filtered = filtered[filtered["neighbourhood"] == selected_area]
        if selected_month != "All":
            filtered = filtered[filtered["year_month"] == selected_month]

        if filtered.empty:
            st.warning("⚠️ No data available for this selection.")
        else:
            avg_price = filtered.groupby("date")["adjusted_price"].mean().reset_index()

            # Chart label
            area_label = selected_area if selected_area != "All" else "All Neighborhoods"
            month_label = selected_month if selected_month != "All" else "June 2024 – June 2025"
            st.subheader(f"📈 {area_label} Price Trend ({month_label})")

            st.line_chart(avg_price.set_index("date"))
            st.dataframe(avg_price)

    except Exception as e:
        st.error(f"❌ Error processing calendar chart: {e}")

# 💬 Section 4: Review Insights
elif section == "Review Insights":
    st.title("💬 Review Engagement by Neighborhood")
    st.write("Top areas with the most guest feedback.")

    try:
        top_reviews = reviews.groupby("neighbourhood")["comments"].count().sort_values(ascending=False).head(10)
        st.bar_chart(top_reviews)
    except Exception as e:
        st.error(f"❌ Error loading review insights: {e}")
