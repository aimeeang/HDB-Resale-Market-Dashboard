# Interactive HDB Resale Market Dashboard

This repository contains the code and resources for the Interactive HDB Resale Market Dashboard. The project uses data from data.gov.sg and the OneMap API to enhance the HDB resale flat dataset with geospatial information.

## Project Features
- **Data Enhancement**: Used Python and the OneMap API to generate missing latitude and longitude data.
- **Proximity Analysis**: Calculated the nearest MRT stations, including distance and walking time for each HDB Resale Flat transaction.
- **Educational and Commercial Insights**: Identified the top 5 closest schools and shopping malls for each flat with Python.
- **Interactive Dashboard**: Power BI dashboard that allows users to explore trends and proximity information.

## Tools and Technologies
- Python
- OneMap API
- Power BI

## Project Files
- `data_cleaning.py`: Python script for cleaning and preparing data.
- `geospatial_analysis.py`: Python script for generating geospatial data.
- `proximity_analysis.py`: Python script for calculating distances to MRT stations, schools, and malls.
- `power_bi_dashboard.pbix`: Power BI dashboard file.
- `README.md`: Project documentation.

## How to Run
1. Clone this repository.
2. Install required libraries (listed in `requirements.txt`).
3. Run the Python scripts to prepare the data.
4. Open the Power BI dashboard file to explore the visualizations.
