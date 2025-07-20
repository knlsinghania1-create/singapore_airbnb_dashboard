# 🇸🇬 Singapore Airbnb Dashboard

An interactive dashboard built with Streamlit to explore Airbnb price trends, guest reviews, and listings across Singapore. Simulated calendar data adds realistic seasonal pricing. Designed for data storytelling, portfolio presentation, and market analysis.

---

## 📊 Features

- 📅 **Smart Calendar Simulation:** Dynamic pricing across June 2024–June 2025 with weekday/weekend + seasonal uplift
- 📈 **Price Trend Visualization:** Filter by neighborhood and month (or view all)
- 🗺️ **Listing Map:** Folium-based map showing location and pricing distribution
- 💬 **Review Engagement:** Charts highlighting top-reviewed neighborhoods
- 🧠 **Modular Scripts:** Step-by-step preprocessing with reproducibility

---

## 🚀 How to Run

### Option 1: Local

1. Clone the repo:
   ```bash
   git clone https://github.com/knlsinghania1-create/singapore_airbnb_dashboard.git
   cd singapore_airbnb_dashboard

2. Setup Env:
conda create -n airbnb_env python=3.9
conda activate airbnb_env
pip install -r requirements.txt

3. Launch Dashboard
streamlit run app.py

Folder Strucutre

├── app.py                    # Streamlit dashboard
├── requirements.txt
├── README.md
├── data/                     # Raw CSV files from Inside Airbnb
├── outputs/                  # Cleaned data, visuals, calendar
├── scripts/                  # Processing + simulation logic
└── streamlit_env/            # Optional: Conda environment setup

