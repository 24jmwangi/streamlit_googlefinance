
## Google Finance Streamlit Dashboard
![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-app-red?logo=streamlit)
![Google Sheets API](https://img.shields.io/badge/Google_Sheets_API-active-brightgreen?logo=google-sheets)
![Google Finance](https://img.shields.io/badge/Google_Finance-data-yellow?logo=google)
![Codespaces](https://img.shields.io/badge/GitHub-Codespaces-lightgrey?logo=github)
![Deployed](https://img.shields.io/badge/Deployed-Streamlit_Cloud-orange?logo=streamlit)


This project is a simple Streamlit app that visualizes stock data pulled from a Google Sheet that updates daily using the `GOOGLEFINANCE` formula.

### Features

- Uses Google Sheets as a data source
- Sheet auto-updates daily with formula  
  `=GOOGLEFINANCE("AAPL", "all", TODAY()-14, TODAY(), "DAILY")`
- Connects to the sheet via Google Sheets API
- Deployed on Streamlit Cloud
- Includes a manual Refresh button to force update

```python
if refresh:
    download_data.clear()
    transform_data.clear()
    st.cache_resource.clear()
    st.rerun()
````

### Live Demo

View the live dashboard below:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gglefinance.streamlit.app/?embed_options=dark_theme,show_footer,show_padding,disable_scrolling,show_colored_line,light_theme,show_toolbar)


### Setup

1. Clone the repository
2. Create a `secrets.toml` file or use `st.secrets` to store your Google service account credentials
3. Install dependencies

   ```
   pip install -r requirements.txt
   ```
4. Run the app

   ```
   streamlit run app.py
   ```

### Deployment

Currently deployed on Streamlit Cloud.

### Next Steps

* Modularize code (separate data download, transformation, and UI)
* Explore other deployment options such as VPS, Google Cloud VM, or Docker
* Add scheduled refresh using Streamlit Community Cloud or external cronjob
* Add more stock symbols and make selection dynamic


